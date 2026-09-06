import json,os
from datetime import datetime
B=os.path.expanduser("~/LyTuongSong_AI")
def L(f):
 try:
  with open(os.path.join(B,f),encoding="utf-8") as x:return json.load(x)
 except:return []
def S(f,d):
 with open(os.path.join(B,f),"w",encoding="utf-8") as x:json.dump(d,x,ensure_ascii=False,indent=2)
def brain():return {"memory":L("memory.json"),"goals":L("goals.json"),"plans":L("plans.json"),"tasks":L("tasks.json")}
def next_task(b):
 for t in b["tasks"]:
  if not t.get("done"):return t.get("name")
def remember(x):
 d=L("memory.json");d.append({"time":datetime.now().isoformat(timespec="seconds"),"content":x});S("memory.json",d)
def run():
 b=brain();t=next_task(b)
 print("\n👑 MANAGER");print("🔎 RESEARCH → Context");print("📋 PLANNER →",t or "Không còn Task")
 if not t:return
 if input("🛡️ Duyệt? (y/n): ").lower()!="y":print("🛑 Dừng.");return
 print("🛠️ EXECUTOR →",t)
 for x in b["tasks"]:
  if x.get("name")==t:x["done"]=True
 S("tasks.json",b["tasks"]);p=round(sum(x.get("done",False) for x in b["tasks"])*100/len(b["tasks"])) if b["tasks"] else 0
 g=L("goals.json")
 if g:g[0]["progress"]=p;S("goals.json",g)
 remember("v7.0 hoàn thành: "+t+"; Progress="+str(p)+"%")
 print("✅ Hoàn tất — Progress:",p,"%")
print("🤖 AI AGENT LÝ TƯỞNG SỐNG v7.0");print("Lệnh: brain | next | run | thoat")
while True:
 q=input("\n👤 Bạn: ").strip().lower()
 if q=="thoat":break
 if q=="brain":
  b=brain();print("🧠 BRAIN | Memory:",len(b["memory"]),"Goals:",len(b["goals"]),"Plans:",len(b["plans"]),"Tasks:",len(b["tasks"]))
 elif q=="next":print("⚙️ Next:",next_task(brain()) or "Không còn Task")
 elif q=="run":run()
 else:print("Dùng: brain | next | run | thoat")
