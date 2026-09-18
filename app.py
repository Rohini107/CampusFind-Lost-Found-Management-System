import os
from datetime import datetime
from functools import wraps
from bson import ObjectId
from flask import Flask, jsonify, render_template, request, redirect, url_for, session, flash
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "campusfind-change-this-secret")
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/campusfind")
mongo = PyMongo(app)

CATEGORIES = ["Electronics","Documents","Books","Bags","Keys","Clothing","Accessories","Other"]
STATUSES = ["Reported","Searching","Matched","Claimed","Closed"]

def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            flash("Please login to continue.", "warning")
            return redirect(url_for("login"))
        return fn(*args, **kwargs)
    return wrapper

def oid(value):
    try: return ObjectId(value)
    except Exception: return None

def serialize(r):
    return {
        "id": str(r["_id"]), "type": r.get("type",""),
        "item_name": r.get("item_name",""), "description": r.get("description",""),
        "category": r.get("category",""), "location": r.get("location",""),
        "date": r.get("date",""), "contact_name": r.get("contact_name",""),
        "contact_phone": r.get("contact_phone",""), "status": r.get("status","Reported")
    }

def similarity(a,b):
    score, reasons = 0, []
    if a.get("category")==b.get("category"):
        score += 35; reasons.append("Same category")
    wa=set((a.get("item_name","")+" "+a.get("description","")).lower().split())
    wb=set((b.get("item_name","")+" "+b.get("description","")).lower().split())
    shared={x for x in wa & wb if len(x)>2}
    if shared:
        score += min(35, len(shared)*7); reasons.append("Similar item details")
    la=a.get("location","").lower().strip(); lb=b.get("location","").lower().strip()
    if la and la==lb:
        score += 20; reasons.append("Same location")
    elif la and lb and (la in lb or lb in la):
        score += 10; reasons.append("Related location")
    if a.get("date") and a.get("date")==b.get("date"):
        score += 10; reasons.append("Same date")
    return min(score,100), reasons

@app.route("/")
def index():
    return render_template("index.html",
        total=mongo.db.reports.count_documents({}),
        lost=mongo.db.reports.count_documents({"type":"Lost"}),
        found=mongo.db.reports.count_documents({"type":"Found"}),
        matched=mongo.db.reports.count_documents({"status":"Matched"}),
        recent=[serialize(x) for x in mongo.db.reports.find().sort("created_at",-1).limit(6)])

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        name=request.form.get("name","").strip()
        email=request.form.get("email","").strip().lower()
        password=request.form.get("password","")
        if not name or not email or len(password)<6:
            flash("Enter all fields. Password must be at least 6 characters.","danger")
        elif mongo.db.users.find_one({"email":email}):
            flash("Email is already registered.","danger")
        else:
            mongo.db.users.insert_one({"name":name,"email":email,
                "password":generate_password_hash(password),"created_at":datetime.utcnow()})
            flash("Account created. Please login.","success")
            return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form.get("email","").strip().lower()
        user=mongo.db.users.find_one({"email":email})
        if user and check_password_hash(user["password"], request.form.get("password","")):
            session["user_id"]=str(user["_id"]); session["user_name"]=user["name"]
            return redirect(url_for("dashboard"))
        flash("Invalid email or password.","danger")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear(); flash("Logged out successfully.","success")
    return redirect(url_for("index"))

@app.route("/dashboard")
@login_required
def dashboard():
    reports=[serialize(x) for x in mongo.db.reports.find({"owner_id":oid(session["user_id"])}).sort("created_at",-1)]
    return render_template("reports.html",reports=reports,categories=CATEGORIES,statuses=STATUSES,dashboard=True)

@app.route("/reports")
@login_required
def reports():
    q=request.args.get("q","").strip(); typ=request.args.get("type","")
    cat=request.args.get("category",""); status=request.args.get("status","")
    query={"owner_id":oid(session["user_id"])}
    if typ: query["type"]=typ
    if cat: query["category"]=cat
    if status: query["status"]=status
    if q: query["$or"]=[{"item_name":{"$regex":q,"$options":"i"}},
        {"description":{"$regex":q,"$options":"i"}},{"location":{"$regex":q,"$options":"i"}}]
    reports=[serialize(x) for x in mongo.db.reports.find(query).sort("created_at",-1)]
    return render_template("reports.html",reports=reports,categories=CATEGORIES,statuses=STATUSES,dashboard=False)

@app.route("/report/new", methods=["GET","POST"])
@login_required
def new_report():
    if request.method=="POST":
        d=request.form
        if not d.get("type") or not d.get("item_name") or not d.get("category") or not d.get("location"):
            flash("Please fill all required fields.","danger")
        else:
            mongo.db.reports.insert_one({
                "type":d["type"],"item_name":d["item_name"].strip(),
                "description":d.get("description","").strip(),"category":d["category"],
                "location":d["location"].strip(),"date":d.get("date",""),
                "contact_name":d.get("contact_name","").strip(),
                "contact_phone":d.get("contact_phone","").strip(),
                "status":"Reported","owner_id":oid(session["user_id"]),"created_at":datetime.utcnow()
            })
            flash("Report added successfully.","success"); return redirect(url_for("reports"))
    return render_template("report_form.html",report=None,categories=CATEGORIES)

@app.route("/report/<rid>/edit", methods=["GET","POST"])
@login_required
def edit_report(rid):
    report=mongo.db.reports.find_one({"_id":oid(rid),"owner_id":oid(session["user_id"])})
    if not report: flash("Report not found.","danger"); return redirect(url_for("reports"))
    if request.method=="POST":
        d=request.form
        mongo.db.reports.update_one({"_id":report["_id"]},{"$set":{
            "type":d["type"],"item_name":d["item_name"].strip(),"description":d.get("description","").strip(),
            "category":d["category"],"location":d["location"].strip(),"date":d.get("date",""),
            "contact_name":d.get("contact_name","").strip(),"contact_phone":d.get("contact_phone","").strip()
        }})
        flash("Report updated.","success"); return redirect(url_for("reports"))
    return render_template("report_form.html",report=serialize(report),categories=CATEGORIES)

@app.post("/report/<rid>/delete")
@login_required
def delete_report(rid):
    result=mongo.db.reports.delete_one({"_id":oid(rid),"owner_id":oid(session["user_id"])})
    flash("Report deleted." if result.deleted_count else "Report not found.",
          "success" if result.deleted_count else "danger")
    return redirect(url_for("reports"))

@app.post("/api/status/<rid>")
@login_required
def update_status(rid):
    status=request.json.get("status","")
    if status not in STATUSES: return jsonify(ok=False),400
    result=mongo.db.reports.update_one({"_id":oid(rid),"owner_id":oid(session["user_id"])},{"$set":{"status":status}})
    return jsonify(ok=result.matched_count==1)

@app.route("/matches/<rid>")
@login_required
def matches(rid):
    lost=mongo.db.reports.find_one({"_id":oid(rid),"owner_id":oid(session["user_id"])})
    if not lost: flash("Report not found.","danger"); return redirect(url_for("reports"))
    scored=[]
    for r in mongo.db.reports.find({"type":{"$ne":lost["type"]}}):
        s,reasons=similarity(lost,r)
        if s>=20: scored.append((s,reasons,serialize(r)))
    scored.sort(key=lambda x:x[0],reverse=True)
    return render_template("matches.html",lost=serialize(lost),matches=scored[:10])

if __name__=="__main__":
    app.run(debug=True)
