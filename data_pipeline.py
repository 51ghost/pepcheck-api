"""
PEPCheck API — Politically Exposed Person Screening Pipeline
"""
import time
class DataCache:
    def __init__(self, ttl=3600):
        self._cache = {}; self._ttl = ttl
    def get(self, key):
        val, ts = self._cache.get(key, (None,0))
        if val and time.time()-ts < self._ttl: return val
        return None
    def set(self, key, val): self._cache[key] = (val, time.time())
cache = DataCache()

PEP_DATABASE = [
    {"id":"PEP-001","name":"Joseph R. Biden","title":"President","country":"USA","pep_level":"Head of State","family_connected":["Hunter Biden"],"status":"Active"},
    {"id":"PEP-002","name":"Donald J. Trump","title":"Former President","country":"USA","pep_level":"Head of State","family_connected":["Donald Trump Jr.","Ivanka Trump","Eric Trump"],"status":"Active"},
    {"id":"PEP-003","name":"Kamala Harris","title":"Vice President","country":"USA","pep_level":"Head of State","family_connected":[],"status":"Active"},
    {"id":"PEP-004","name":"Olaf Scholz","title":"Chancellor","country":"Germany","pep_level":"Head of Government","family_connected":[],"status":"Active"},
    {"id":"PEP-005","name":"Emmanuel Macron","title":"President","country":"France","pep_level":"Head of State","family_connected":["Brigitte Macron"],"status":"Active"},
    {"id":"PEP-006","name":"Keir Starmer","title":"Prime Minister","country":"United Kingdom","pep_level":"Head of Government","family_connected":[],"status":"Active"},
    {"id":"PEP-007","name":"Justin Trudeau","title":"Prime Minister","country":"Canada","pep_level":"Head of Government","family_connected":["Pierre Trudeau"],"status":"Active"},
    {"id":"PEP-008","name":"Narendra Modi","title":"Prime Minister","country":"India","pep_level":"Head of Government","family_connected":[],"status":"Active"},
    {"id":"PEP-009","name":"Ursula von der Leyen","title":"EU Commission President","country":"EU","pep_level":"International Organization Head","family_connected":[],"status":"Active"},
    {"id":"PEP-010","name":"Janet Yellen","title":"Treasury Secretary","country":"USA","pep_level":"Minister","family_connected":["George Akerlof"],"status":"Active"},
    {"id":"PEP-011","name":"Jerome Powell","title":"Fed Chair","country":"USA","pep_level":"Central Bank Head","family_connected":[],"status":"Active"},
    {"id":"PEP-012","name":"Antony Blinken","title":"Secretary of State","country":"USA","pep_level":"Minister","family_connected":[],"status":"Active"},
    {"id":"PEP-013","name":"Lloyd Austin","title":"Secretary of Defense","country":"USA","pep_level":"Minister","family_connected":[],"status":"Active"},
    {"id":"PEP-014","name":"Christopher Wray","title":"FBI Director","country":"USA","pep_level":"Senior Official","family_connected":[],"status":"Active"},
    {"id":"PEP-015","name":"Xi Jinping","title":"President","country":"China","pep_level":"Head of State","family_connected":["Peng Liyuan"],"status":"Active"},
]

def check_pep(name):
    name = name.lower()
    matches = [p for p in PEP_DATABASE if name in p["name"].lower()]
    return {"matches": matches, "total": len(matches), "risk_level": "HIGH" if matches else "LOW"}

def search_peps(query="", country=None):
    results = [p for p in PEP_DATABASE if query.lower() in p["name"].lower() or query.lower() in p["title"].lower()]
    if country: results = [p for p in results if country.lower() in p["country"].lower()]
    return results
