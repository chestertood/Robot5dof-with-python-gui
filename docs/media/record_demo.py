"""Regenerate docs/media/demo.gif (Windows, run: python docs/media/record_demo.py).
Drive UI_for_robot.py headlessly-ish, grab frames, build docs/media/demo.gif.
MySQL + Arduino are stubbed so the demo runs anywhere."""
import ctypes, os, sys, time, types
ctypes.windll.shcore.SetProcessDpiAwareness(1)
from PIL import Image, ImageDraw, ImageFont, ImageGrab

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GUI = os.path.join(REPO, "python_gui")
OUT = os.path.join(REPO, "docs", "media", "demo.gif")
sys.path.insert(0, GUI)
os.chdir(GUI)

# --- stub database (no MySQL needed for the demo) ---
class _Cur:
    def execute(self, *a): pass
    def fetchall(self): return []
fake = types.ModuleType("database")
fake.connect_sql = lambda f: (lambda *a, **k: f(_Cur(), *a, **k))
sys.modules["database"] = fake

src = open(os.path.join(GUI, "UI_for_robot.py"), encoding="utf-8").read()
src = src.replace("1920x1080", "1420x800+0+0").replace("root.mainloop()", "")
ns = {"__file__": os.path.join(GUI, "UI_for_robot.py"), "__name__": "ui"}
exec(compile(src, "UI_for_robot.py", "exec"), ns)
root = ns["root"]
root.attributes("-topmost", True)

W, H = 1420, 800
SCALE = 1000 / W
font = ImageFont.truetype("segoeui.ttf", 30)
frames, durs = [], []


def snap(caption, hold=120, box=None):
    root.update(); time.sleep(0.04); root.update()
    x, y = root.winfo_rootx(), root.winfo_rooty()
    im = ImageGrab.grab(bbox=(x, y, x + W, y + H)).convert("RGB")
    im2 = Image.new("RGB", (W, H + 56), "#111827"); im2.paste(im, (0, 0)); im = im2
    d = ImageDraw.Draw(im)
    if box is not None:
        bx, by = box.winfo_rootx() - x, box.winfo_rooty() - y
        d.rectangle([bx - 4, by - 4, bx + box.winfo_width() + 4, by + box.winfo_height() + 4],
                    outline="#e11d48", width=4)
    d.text((20, H + 6), caption, font=font, fill="white")
    im = im.resize((1000, int((H + 56) * SCALE)), Image.LANCZOS)
    frames.append(im); durs.append(hold)


def type_into(entry, text, caption):
    entry.focus_force()
    for i in range(1, len(text) + 1):
        entry.delete(0, "end"); entry.insert(0, text[:i])
    snap(caption, 350, entry)


def click(btn, caption, hold):
    snap(caption, 350, btn)
    btn.invoke()
    snap(caption, hold)


get = lambda n: ns[n]
thetas = ["30", "45", "60", "30", "0"]
snap("Robot5DOF controller", 1200)

# 1) forward kinematics
for i, t in enumerate(thetas, 1):
    type_into(get(f"box_THETA{i}"), t, f"Forward kinematics: enter THETA{i}")
click(get("button_theta"), "SUBMIT -> end-effector pose (R, p)", 1800)

# 2) inverse kinematics: feed the pose back in, read back the joint angles
names = ["r11", "r12", "r13", "px", "r21", "r22", "r23", "py", "r31", "r32", "r33", "pz"]
for n in names:
    shown = root.nametowidget(n).cget("text")
    type_into(get(f"box_{n}"), shown, "Inverse kinematics: enter pose (R, p)")
click(get("button1"), "SUBMIT -> joint angles theta1..theta5", 2500)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
# shared palette keeps size down and avoids per-frame flicker
pal = frames[-1].quantize(256, method=Image.MEDIANCUT)
q = [f.quantize(palette=pal, dither=Image.NONE) for f in frames]
q[0].save(OUT, save_all=True, append_images=q[1:], duration=durs, loop=0, optimize=True)
print("frames", len(q), "size KB", os.path.getsize(OUT) // 1024)
root.destroy()
