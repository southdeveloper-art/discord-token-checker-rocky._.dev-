# 🔍 Discord Token Checker — by rocky._.dev

<div align="center">

```
██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
```

**Professional Discord Token Checker — By rocky._.dev to fuck market**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Version](https://img.shields.io/badge/Version-3.0-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Made by](https://img.shields.io/badge/Made%20by-rocky._.dev-red?style=for-the-badge)

</div>

---

## 📋 Features

- ✅ **Token Validation** — Instantly checks if tokens are valid, invalid, or locked
- 💎 **Nitro Detection** — Detects Nitro Classic, Nitro Boost, and Basic plans
- ⚡ **Boost Tracking** — Shows active boost slot counts per token
- 💳 **Billing Detection** — Identifies accounts with linked payment methods
- 🔐 **2FA Detection** — Flags accounts with Two-Factor Authentication enabled
- 📱 **Phone Verification Check** — Detects phone-verified accounts
- ✉️ **Email Status** — Verified / Unverified / Locked email detection
- 👥 **Friends & Guilds Count** — Shows how many servers and friends each account has
- ⏱️ **Account Age** — Categorizes accounts by age (30d+, 90d+, 365d+)
- ⭐ **HQ & Premium HQ Sorting** — Automatically sorts high-quality accounts
- 🎨 **Rich Console Output** — Color-coded, single-line output per token
- 💾 **Auto Save Results** — All results are saved to categorized `.txt` files

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip

### Setup

```bash
# Clone the repo
git clone https://github.com/southdeveloper-art/discord-token-checker-rocky._.dev-.git
cd discord-token-checker-rocky._.dev-

# Install dependencies
pip install requests colorama
```

---

## 📂 Usage

### 1. Add Tokens to `tokens.txt`

The checker supports **three token formats**:

```
# Format 1: Token only
MTxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Format 2: email:password:token
user@email.com:password123:MTxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Format 3: Mixed (both formats in one file are fine)
```

### 2. Run the Checker

```bash
python main.py
```

That's it! All results are automatically saved to the `results/` folder.

---

## 🖥️ Commands

| Command | Description |
|---|---|
| `python main.py` | Run the token checker (reads `tokens.txt`) |

> **Made by rocky._.dev** — All output is branded and logged automatically.

---

## 📁 Output Files

After running, the `results/` folder will contain:

| File | Description |
|---|---|
| `valid.txt` | All valid tokens with full account info |
| `invalid.txt` | Invalid / expired tokens |
| `locked.txt` | Locked / disabled accounts |
| `nitro.txt` | Tokens with any Nitro subscription |
| `no_nitro.txt` | Tokens without Nitro |
| `phone_verified.txt` | Phone-verified accounts |
| `phone_locked.txt` | Accounts without phone verification |
| `email_verified.txt` | Email-verified accounts |
| `email_locked.txt` | Accounts without email |
| `email_unverified.txt` | Unverified email accounts |
| `boost_alive.txt` | Accounts with active boost slots |
| `boost_dead.txt` | Accounts without boosts |
| `with_billing.txt` | Accounts with linked payment methods |
| `with_2fa.txt` | Accounts with 2FA enabled |
| `aged_30plus.txt` | Accounts older than 30 days |
| `aged_90plus.txt` | Accounts older than 90 days |
| `aged_365plus.txt` | Accounts older than 1 year |
| `with_friends.txt` | Accounts with at least 1 friend |
| `in_guilds.txt` | Accounts that are in servers |
| `hq.txt` | HQ accounts (phone + email + billing/nitro) |
| `premium_hq.txt` | Premium HQ (all HQ criteria + 2FA + 90d+ + friends) |

---

## 📊 Console Output Format

Each token is displayed in a single compact line:

```
[i/total] TOKEN**** [✓ VALID] | @username | AGEd | 📱 Phone | ✓ Email | 💎 Nitro | ⚡Boosts | 💳 Bill | 🔐 2FA | 🏠Guilds | 👥Friends | 🖼️🎨📝
```

| Badge | Meaning |
|---|---|
| `[✓ VALID]` | Token is active and working |
| `[✗ INVALID]` | Token is expired or invalid |
| `[⚠ LOCKED]` | Account is locked/disabled |
| `📱 Phone` | Phone verified |
| `🚫 NoPhone` | No phone linked |
| `✓ Email` | Email verified |
| `🔒 EmailLock` | Account has no email |
| `💎 Classic` | Nitro Classic |
| `🚀 Nitro` | Nitro Boost |
| `⭐ Basic` | Nitro Basic |
| `⚡ Nx` | N active boost slots |
| `💳 Bill` | Has billing info |
| `🔐 2FA` | 2FA enabled |

---

## ⚙️ Configuration

No configuration needed — just drop your tokens in `tokens.txt` and run.

The tool has a **0.5 second delay** between each token check to avoid rate limiting.

---

## ⚠️ Disclaimer

This tool is for **educational purposes only**. Do not use this tool on tokens you do not own. The author is not responsible for any misuse or violation of Discord's Terms of Service.

---

## 👤 Author

**rocky._.dev**  
Professional Edition v3.0

---

<div align="center">

Made with ♥ by **rocky._.dev**

See [COPYRIGHT](./COPYRIGHT) for license and usage terms.

</div>
