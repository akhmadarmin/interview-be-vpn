from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.conf import settings
import hmac
from hashlib import sha256

class CustomPBKDF2PasswordHasher(PBKDF2PasswordHasher):
    algoritma = "pbkdf2_sha256_with_secret"

    def encode(self, password, salt, buat_hash=None):
        buat_hash = buat_hash or self.buat_hash
        secret_key = settings.SECRET_KEY.encode('utf-8')
        hash = super().encode(password, salt, buat_hash)
        hash_hmac = hmac.new(secret_key, hash.encode('utf-8'), sha256).hexdigest()
        return f"{self.algoritma}${buat_hash}${salt}${hash_hmac}"

    def verifikasi(self, password, encoded):
        try:
            algoritma, buat_hash, salt, hash_hmac = encoded.split('$', 3)
            if algoritma != self.algoritma:
                return False
            hash_baru = self.encode(password, salt, int(buat_hash))
            return hmac.compare_digest(hash_baru, encoded)
        except Exception:
            return False