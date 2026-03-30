# made by rocky._.dev to fuck market
import requests
import json
import os
from datetime import datetime
from colorama import Fore, Style, init
import time

init(autoreset=True)

class DiscordTokenChecker:
    def __init__(self):
        self.results = {
            'valid': [],
            'invalid': [],
            'locked': [],
            'nitro': [],
            'no_nitro': [],
            'phone_verified': [],
            'phone_locked': [],
            'email_verified': [],
            'email_locked': [],
            'email_unverified': [],
            'boost_alive': [],
            'boost_dead': [],
            'hq': [],
            'with_billing': [],
            'with_2fa': [],
            'aged_30plus': [],
            'aged_90plus': [],
            'aged_365plus': [],
            'with_friends': [],
            'in_guilds': [],
            'premium_hq': []
        }
        
        if not os.path.exists('results'):
            os.makedirs('results')
        
        self.session = requests.Session()
    
    def print_banner(self):
        banner = f"""
{Fore.LIGHTCYAN_EX}╔═══════════════════════════════════════════════════════════════╗
{Fore.LIGHTCYAN_EX}║                                                               ║
{Fore.LIGHTCYAN_EX}║  ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗        ║
{Fore.LIGHTCYAN_EX}║  ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗       ║
{Fore.LIGHTCYAN_EX}║  ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║       ║
{Fore.LIGHTCYAN_EX}║  ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║       ║
{Fore.LIGHTCYAN_EX}║  ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝       ║
{Fore.LIGHTCYAN_EX}║  ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝        ║
{Fore.LIGHTCYAN_EX}║                                                               ║
{Fore.LIGHTCYAN_EX}║              {Fore.LIGHTMAGENTA_EX}TOKEN CHECKER - Made by rocky._.dev {Fore.LIGHTCYAN_EX}              ║
{Fore.LIGHTCYAN_EX}║                  {Fore.WHITE}Professional Edition v3.0{Fore.LIGHTCYAN_EX}                   ║
{Fore.LIGHTCYAN_EX}║                                                               ║
{Fore.LIGHTCYAN_EX}╚═══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
        """
        print(banner)
    # made by rocky._.dev to fuck market
    def parse_token_line(self, line):
        """Parse different token formats"""
        line = line.strip()
        if not line:
            return None, None, None
        
        # Format: email:pass:token
        if line.count(':') >= 2:
            parts = line.split(':')
            if len(parts) >= 3:
                email = parts[0]
                password = parts[1]
                token = ':'.join(parts[2:])
                return token, email, password
        
        # Format: token only
        return line, None, None
    
    def mask_token(self, token):
        """Mask token for display"""
        if len(token) > 20:
            return token[:14] + "****"
        return token[:8] + "****"
    
    def get_status_badge(self, status_type, value):
        """Generate colored status badges"""
        badges = {
            'valid': f"{Fore.BLACK}[{Fore.GREEN}✓ VALID{Fore.BLACK}]{Fore.WHITE}",
            'invalid': f"{Fore.BLACK}[{Fore.RED}✗ INVALID{Fore.BLACK}]{Fore.WHITE}",
            'locked': f"{Fore.BLACK}[{Fore.YELLOW}⚠ LOCKED{Fore.BLACK}]{Fore.WHITE}",
            'timeout': f"{Fore.BLACK}[{Fore.YELLOW}⏱ TIMEOUT{Fore.BLACK}]{Fore.WHITE}",
            'error': f"{Fore.BLACK}[{Fore.RED}⚠ ERROR{Fore.BLACK}]{Fore.WHITE}",
            
            'phone_yes': f"{Fore.GREEN}📱 Phone{Fore.WHITE}",
            'phone_no': f"{Fore.RED}🚫 NoPhone{Fore.WHITE}",
            
            'email_verified': f"{Fore.GREEN}✓ Email{Fore.WHITE}",
            'email_locked': f"{Fore.YELLOW}🔒 EmailLock{Fore.WHITE}",
            'email_unverified': f"{Fore.RED}✗ Email{Fore.WHITE}",
            'email_none': f"{Fore.RED}🚫 NoEmail{Fore.WHITE}",
            
            'nitro_classic': f"{Fore.LIGHTMAGENTA_EX}💎 Classic{Fore.WHITE}",
            'nitro_boost': f"{Fore.LIGHTMAGENTA_EX}🚀 Nitro{Fore.WHITE}",
            'nitro_basic': f"{Fore.LIGHTMAGENTA_EX}⭐ Basic{Fore.WHITE}",
            'nitro_none': f"{Fore.WHITE}○ NoNitro{Fore.WHITE}",
            
            'boost_yes': f"{Fore.LIGHTCYAN_EX}⚡{value}x{Fore.WHITE}",
            'boost_no': f"{Fore.WHITE}○ NoBoost{Fore.WHITE}",
            
            'billing_yes': f"{Fore.LIGHTCYAN_EX}💳 Bill{Fore.WHITE}",
            'billing_no': f"{Fore.WHITE}○ NoBill{Fore.WHITE}",
            
            '2fa_yes': f"{Fore.LIGHTRED_EX}🔐 2FA{Fore.WHITE}",
            '2fa_no': f"{Fore.WHITE}○ No2FA{Fore.WHITE}",
            
            'guilds': f"{Fore.LIGHTBLUE_EX}🏠{value}{Fore.WHITE}",
            'friends': f"{Fore.LIGHTGREEN_EX}👥{value}{Fore.WHITE}",
        }
        return badges.get(status_type, value)
    # made by rocky._.dev to fuck market
    def check_token(self, token, email=None, password=None):
        """Check token using multiple safe endpoints"""
        masked_token = self.mask_token(token)
        
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        try:
            # Use /users/@me/settings endpoint
            r = self.session.get(
                'https://discord.com/api/v9/users/@me/settings',
                headers=headers,
                timeout=10
            )
            
            # Check for locked/disabled account
            if r.status_code == 401:
                print(f"{masked_token} {self.get_status_badge('invalid', None)}")
                self.results['invalid'].append(f"{email}:{password}:{token}" if email else token)
                return None
            
            elif r.status_code == 403:
                print(f"{masked_token} {self.get_status_badge('locked', None)}")
                self.results['locked'].append(f"{email}:{password}:{token}" if email else token)
                return None
            
            elif r.status_code != 200:
                print(f"{masked_token} {self.get_status_badge('error', None)} [Status: {r.status_code}]")
                self.results['invalid'].append(f"{email}:{password}:{token}" if email else token)
                return None
            
            # Get user info
            user_r = self.session.get(
                'https://discord.com/api/v9/users/@me',
                headers=headers,
                timeout=10
            )
            
            if user_r.status_code != 200:
                print(f"{masked_token} {self.get_status_badge('invalid', None)}")
                self.results['invalid'].append(f"{email}:{password}:{token}" if email else token)
                return None
            
            user_data = user_r.json()
            settings_data = r.json()
            
            # Extract data
            username = user_data.get('username', 'Unknown')
            user_id = user_data.get('id', 'Unknown')
            user_email = user_data.get('email', None)
            phone = user_data.get('phone', None)
            verified = user_data.get('verified', False)
            mfa_enabled = user_data.get('mfa_enabled', False)
            nitro_type = user_data.get('premium_type', 0)
            avatar = user_data.get('avatar', None)
            banner = user_data.get('banner', None)
            bio = user_data.get('bio', '')
            
            # Calculate account age
            timestamp = int(user_id) >> 22
            created_at = datetime.fromtimestamp(timestamp / 1000 + 1420070400)
            age_days = (datetime.now() - created_at).days
            
            # Get guilds count
            guild_count = 0
            try:
                guilds_r = self.session.get(
                    'https://discord.com/api/v9/users/@me/guilds',
                    headers=headers,
                    timeout=5
                )
                if guilds_r.status_code == 200:
                    guilds = guilds_r.json()
                    guild_count = len(guilds)
            except:
                pass
            
            # Get friends count
            friends_count = 0
            try:
                friends_r = self.session.get(
                    'https://discord.com/api/v9/users/@me/relationships',
                    headers=headers,
                    timeout=5
                )
                if friends_r.status_code == 200:
                    relationships = friends_r.json()
                    # Type 1 = friends, 2 = blocked, 3 = incoming request, 4 = outgoing request
                    friends_count = len([r for r in relationships if r.get('type') == 1])
            except:
                pass
            
            # Determine statuses
            # Phone Status
            if phone:
                phone_badge = self.get_status_badge('phone_yes', None)
                self.results['phone_verified'].append(f"{email}:{password}:{token}" if email else token)
            else:
                phone_badge = self.get_status_badge('phone_no', None)
                self.results['phone_locked'].append(f"{email}:{password}:{token}" if email else token)
            
            # Email Status
            if user_email is None:
                email_badge = self.get_status_badge('email_none', None)
                self.results['email_locked'].append(f"{email}:{password}:{token}" if email else token)
            elif not verified:
                email_badge = self.get_status_badge('email_unverified', None)
                self.results['email_unverified'].append(f"{email}:{password}:{token}" if email else token)
            else:
                email_badge = self.get_status_badge('email_verified', None)
                self.results['email_verified'].append(f"{email}:{password}:{token}" if email else token)
            
            # Nitro status
            if nitro_type == 1:
                nitro_badge = self.get_status_badge('nitro_classic', None)
                self.results['nitro'].append(f"{email}:{password}:{token}" if email else token)
            elif nitro_type == 2:
                nitro_badge = self.get_status_badge('nitro_boost', None)
                self.results['nitro'].append(f"{email}:{password}:{token}" if email else token)
            elif nitro_type == 3:
                nitro_badge = self.get_status_badge('nitro_basic', None)
                self.results['nitro'].append(f"{email}:{password}:{token}" if email else token)
            else:
                nitro_badge = self.get_status_badge('nitro_none', None)
                self.results['no_nitro'].append(f"{email}:{password}:{token}" if email else token)
            
            # Check billing
            has_billing = False
            try:
                billing_r = self.session.get(
                    'https://discord.com/api/v9/users/@me/billing/payment-sources',
                    headers=headers,
                    timeout=5
                )
                if billing_r.status_code == 200:
                    billing_data = billing_r.json()
                    if len(billing_data) > 0:
                        has_billing = True
            except:
                pass
            
            billing_badge = self.get_status_badge('billing_yes' if has_billing else 'billing_no', None)
            
            # Check boosts
            boost_count = 0
            try:
                boost_r = self.session.get(
                    'https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots',
                    headers=headers,
                    timeout=5
                )
                if boost_r.status_code == 200:
                    boosts = boost_r.json()
                    boost_count = len(boosts)
            except:
                pass
            # made by rocky._.dev to fuck market
            if boost_count > 0:
                boost_badge = self.get_status_badge('boost_yes', boost_count)
                self.results['boost_alive'].append(f"{email}:{password}:{token}" if email else token)
            else:
                boost_badge = self.get_status_badge('boost_no', None)
                self.results['boost_dead'].append(f"{email}:{password}:{token}" if email else token)
            
            # 2FA Badge
            twofa_badge = self.get_status_badge('2fa_yes' if mfa_enabled else '2fa_no', None)
            
            # Guilds and Friends badges
            guilds_badge = self.get_status_badge('guilds', guild_count)
            friends_badge = self.get_status_badge('friends', friends_count)
            
            # Build clean single-line log with ALL info
            has_avatar = "🖼️" if avatar else "○"
            has_banner = "🎨" if banner else "○"
            has_bio = "📝" if bio else "○"
            
            log_line = (f"{masked_token} {self.get_status_badge('valid', None)} | "
                       f"{Fore.CYAN}@{username}{Fore.WHITE} | "
                       f"{Fore.YELLOW}{age_days}d{Fore.WHITE} | "
                       f"{phone_badge} | {email_badge} | "
                       f"{nitro_badge} | {boost_badge} | "
                       f"{billing_badge} | {twofa_badge} | "
                       f"{guilds_badge} | {friends_badge} | "
                       f"{Fore.LIGHTMAGENTA_EX}{has_avatar}{has_banner}{has_bio}{Fore.WHITE}")
            
            print(log_line)
            # made by rocky._.dev to fuck market
            # Save to results
            save_format = f"{email}:{password}:{token} | {username} | {user_id} | Age:{age_days}d | Guilds:{guild_count} | Friends:{friends_count}" if email else f"{token} | {username} | {user_id} | Age:{age_days}d | Guilds:{guild_count} | Friends:{friends_count}"
            self.results['valid'].append(save_format)
            
            # Track billing
            if has_billing:
                self.results['with_billing'].append(save_format)
            
            # Track 2FA
            if mfa_enabled:
                self.results['with_2fa'].append(save_format)
            
            # Track aged accounts
            if age_days >= 30:
                self.results['aged_30plus'].append(save_format)
            if age_days >= 90:
                self.results['aged_90plus'].append(save_format)
            if age_days >= 365:
                self.results['aged_365plus'].append(save_format)
            
            # Track accounts with friends
            if friends_count > 0:
                self.results['with_friends'].append(save_format)
            
            # Track accounts in guilds
            if guild_count > 0:
                self.results['in_guilds'].append(save_format)
            
            # Check if HQ (phone + email verified + (billing or nitro))
            if phone and verified and user_email and (has_billing or nitro_type > 0):
                self.results['hq'].append(save_format)
            
            # Premium HQ: phone + email + billing + nitro + 2fa + aged 90+ + friends
            if phone and verified and user_email and has_billing and nitro_type > 0 and mfa_enabled and age_days >= 90 and friends_count > 0:
                self.results['premium_hq'].append(save_format)
            
            return user_data
            # made by rocky._.dev to fuck market
        except requests.exceptions.Timeout:
            print(f"{masked_token} {self.get_status_badge('timeout', None)}")
            self.results['invalid'].append(token)
            return None
        except Exception as e:
            print(f"{masked_token} {self.get_status_badge('error', None)} [{str(e)[:30]}]")
            self.results['invalid'].append(token)
            return None
    
    def save_results(self):
        print(f"\n{Fore.LIGHTCYAN_EX}{'═' * 63}")
        print(f"{Fore.LIGHTCYAN_EX}[{Fore.WHITE}💾 SAVING RESULTS{Fore.LIGHTCYAN_EX}]{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}{'═' * 63}{Style.RESET_ALL}\n")
        
        files_map = {
            'valid.txt': self.results['valid'],
            'invalid.txt': self.results['invalid'],
            'locked.txt': self.results['locked'],
            'nitro.txt': self.results['nitro'],
            'no_nitro.txt': self.results['no_nitro'],
            'phone_verified.txt': self.results['phone_verified'],
            'phone_locked.txt': self.results['phone_locked'],
            'email_verified.txt': self.results['email_verified'],
            'email_locked.txt': self.results['email_locked'],
            'email_unverified.txt': self.results['email_unverified'],
            'boost_alive.txt': self.results['boost_alive'],
            'boost_dead.txt': self.results['boost_dead'],
            'hq.txt': self.results['hq'],
            'premium_hq.txt': self.results['premium_hq'],
            'with_billing.txt': self.results['with_billing'],
            'with_2fa.txt': self.results['with_2fa'],
            'aged_30plus.txt': self.results['aged_30plus'],
            'aged_90plus.txt': self.results['aged_90plus'],
            'aged_365plus.txt': self.results['aged_365plus'],
            'with_friends.txt': self.results['with_friends'],
            'in_guilds.txt': self.results['in_guilds']
        }
        
        for filename, data in files_map.items():
            filepath = os.path.join('results', filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                for line in data:
                    f.write(line + '\n')
            
            if len(data) > 0:
                print(f"  {Fore.GREEN}✓{Fore.WHITE} {filename:<25} {Fore.YELLOW}({len(data)} tokens){Style.RESET_ALL}")
        
        print(f"\n{Fore.LIGHTCYAN_EX}{'═' * 63}{Style.RESET_ALL}")
    
    def run(self):
        self.print_banner()
        
        if not os.path.exists('tokens.txt'):
            print(f"{Fore.RED}[ERROR] {Fore.WHITE}tokens.txt not found! Create it and add tokens.{Style.RESET_ALL}")
            return
        
        with open('tokens.txt', 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        
        if len(lines) == 0:
            print(f"{Fore.RED}[ERROR] {Fore.WHITE}No tokens found in tokens.txt!{Style.RESET_ALL}")
            return
        
        print(f"{Fore.LIGHTCYAN_EX}[{Fore.WHITE}INFO{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Loaded {Fore.YELLOW}{len(lines)}{Fore.WHITE} tokens")
        print(f"{Fore.LIGHTCYAN_EX}[{Fore.WHITE}INFO{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Starting token verification...")
        print(f"{Fore.LIGHTCYAN_EX}{'═' * 63}{Style.RESET_ALL}\n")
        
        for i, line in enumerate(lines, 1):
            print(f"{Fore.LIGHTCYAN_EX}[{Fore.YELLOW}{i}{Fore.WHITE}/{Fore.YELLOW}{len(lines)}{Fore.LIGHTCYAN_EX}]{Fore.WHITE} ", end='')
            token, email, password = self.parse_token_line(line)
            
            if token:
                self.check_token(token, email, password)
                time.sleep(0.5)
            else:
                print(f"INVALID FORMAT")
        
        self.save_results()
        
        # Print summary
        print(f"\n{Fore.LIGHTCYAN_EX}╔═══════════════════════════════════════════════════════════════╗")
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.YELLOW}                          SUMMARY                              {Fore.LIGHTCYAN_EX}║")
        print(f"{Fore.LIGHTCYAN_EX}╠═══════════════════════════════════════════════════════════════╣{Style.RESET_ALL}")
        
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.WHITE}  {Fore.GREEN}✓ Valid Tokens:{' ' * 11}{Fore.YELLOW}{len(self.results['valid']):>4}{Fore.WHITE} tokens             {Fore.LIGHTCYAN_EX}║{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.WHITE}  {Fore.RED}✗ Invalid Tokens:{' ' * 9}{Fore.YELLOW}{len(self.results['invalid']):>4}{Fore.WHITE} tokens             {Fore.LIGHTCYAN_EX}║{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.WHITE}  {Fore.YELLOW}⚠ Locked Tokens:{' ' * 10}{Fore.YELLOW}{len(self.results['locked']):>4}{Fore.WHITE} tokens             {Fore.LIGHTCYAN_EX}║{Style.RESET_ALL}")
        
        print(f"{Fore.LIGHTCYAN_EX}╠═══════════════════════════════════════════════════════════════╣{Style.RESET_ALL}")
        
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.WHITE}  {Fore.LIGHTMAGENTA_EX}💎 With Nitro:{' ' * 12}{Fore.YELLOW}{len(self.results['nitro']):>4}{Fore.WHITE} tokens             {Fore.LIGHTCYAN_EX}║{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.WHITE}  {Fore.LIGHTCYAN_EX}⚡ With Boosts:{' ' * 11}{Fore.YELLOW}{len(self.results['boost_alive']):>4}{Fore.WHITE} tokens             {Fore.LIGHTCYAN_EX}║{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.WHITE}  {Fore.LIGHTCYAN_EX}💳 With Billing:{' ' * 10}{Fore.YELLOW}{len(self.results['with_billing']):>4}{Fore.WHITE} tokens             {Fore.LIGHTCYAN_EX}║{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.WHITE}  {Fore.LIGHTRED_EX}🔐 With 2FA:{' ' * 14}{Fore.YELLOW}{len(self.results['with_2fa']):>4}{Fore.WHITE} tokens             {Fore.LIGHTCYAN_EX}║{Style.RESET_ALL}")
        
        print(f"{Fore.LIGHTCYAN_EX}╠═══════════════════════════════════════════════════════════════╣{Style.RESET_ALL}")
        
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.WHITE}  {Fore.GREEN}📱 Phone Verified:{' ' * 8}{Fore.YELLOW}{len(self.results['phone_verified']):>4}{Fore.WHITE} tokens             {Fore.LIGHTCYAN_EX}║{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.WHITE}  {Fore.RED}🚫 Phone Locked:{' ' * 10}{Fore.YELLOW}{len(self.results['phone_locked']):>4}{Fore.WHITE} tokens             {Fore.LIGHTCYAN_EX}║{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.WHITE}  {Fore.GREEN}✓ Email Verified:{' ' * 8}{Fore.YELLOW}{len(self.results['email_verified']):>4}{Fore.WHITE} tokens             {Fore.LIGHTCYAN_EX}║{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.WHITE}  {Fore.YELLOW}🔒 Email Locked:{' ' * 10}{Fore.YELLOW}{len(self.results['email_locked']):>4}{Fore.WHITE} tokens             {Fore.LIGHTCYAN_EX}║{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.WHITE}  {Fore.RED}✗ Email Unverified:{' ' * 6}{Fore.YELLOW}{len(self.results['email_unverified']):>4}{Fore.WHITE} tokens             {Fore.LIGHTCYAN_EX}║{Style.RESET_ALL}")
        
        print(f"{Fore.LIGHTCYAN_EX}╠═══════════════════════════════════════════════════════════════╣{Style.RESET_ALL}")
        
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.WHITE}  {Fore.LIGHTGREEN_EX}👥 With Friends:{' ' * 10}{Fore.YELLOW}{len(self.results['with_friends']):>4}{Fore.WHITE} tokens             {Fore.LIGHTCYAN_EX}║{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.WHITE}  {Fore.LIGHTBLUE_EX}🏠 In Guilds:{' ' * 13}{Fore.YELLOW}{len(self.results['in_guilds']):>4}{Fore.WHITE} tokens             {Fore.LIGHTCYAN_EX}║{Style.RESET_ALL}")
        
        print(f"{Fore.LIGHTCYAN_EX}╠═══════════════════════════════════════════════════════════════╣{Style.RESET_ALL}")
        
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.WHITE}  {Fore.YELLOW}⏱ Aged 30+ Days:{' ' * 9}{Fore.YELLOW}{len(self.results['aged_30plus']):>4}{Fore.WHITE} tokens             {Fore.LIGHTCYAN_EX}║{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.WHITE}  {Fore.YELLOW}⏱ Aged 90+ Days:{' ' * 9}{Fore.YELLOW}{len(self.results['aged_90plus']):>4}{Fore.WHITE} tokens             {Fore.LIGHTCYAN_EX}║{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.WHITE}  {Fore.YELLOW}⏱ Aged 365+ Days:{' ' * 8}{Fore.YELLOW}{len(self.results['aged_365plus']):>4}{Fore.WHITE} tokens             {Fore.LIGHTCYAN_EX}║{Style.RESET_ALL}")
        
        print(f"{Fore.LIGHTCYAN_EX}╠═══════════════════════════════════════════════════════════════╣{Style.RESET_ALL}")
        
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.WHITE}  {Fore.LIGHTBLUE_EX}⭐ HQ Tokens:{' ' * 13}{Fore.YELLOW}{len(self.results['hq']):>4}{Fore.WHITE} tokens             {Fore.LIGHTCYAN_EX}║{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}║{Fore.WHITE}  {Fore.LIGHTMAGENTA_EX}👑 Premium HQ:{' ' * 12}{Fore.YELLOW}{len(self.results['premium_hq']):>4}{Fore.WHITE} tokens             {Fore.LIGHTCYAN_EX}║{Style.RESET_ALL}")
        
        print(f"{Fore.LIGHTCYAN_EX}╚═══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        print(f"\n{Fore.LIGHTMAGENTA_EX}Made with ♥ by rocky._.dev | Professional Edition v3.0{Style.RESET_ALL}\n")

if __name__ == '__main__':
    checker = DiscordTokenChecker()
    checker.run()
    
    # made by rocky._.dev to fuck market