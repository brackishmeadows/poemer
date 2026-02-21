# -*- coding: utf-8 -*-
import random
import numpy as np
from collections import defaultdict, Counter

# ============================================================
# 0. RNG (optional: uncomment to lock runs)
# ============================================================
# random.seed(42)
# np.random.seed(42)

# ============================================================
# 1. CORPUS
# ============================================================

corpus = [

    # --- high myth ---
    "dragon sleeps beneath the ruined tower",
    "magic flows through the forest like slow fire",
    "map is wrong and the road is hungry",
    "castle stands silent while banners rot",
    "fire dances in the dark and names the dead",
    "door appears where there was only stone",
    "wind crosses the road and unnames the city",
    "embers turn to salt where the river refuses",
    "frost leans inward under broken glass",
    "wolf listens while the night remembers",

    "river bends through ash and broken iron",
    "stars fall quietly behind the western gate",
    "lantern burns low in the abandoned hall",
    "stone remembers every oath it swallowed",
    "witch walks softly across the frozen marsh",
    "forest breathes beneath the shattered moon",
    "blade hums faintly in the silent chapel",
    "road splits where the old king vanished",
    "crow circles above the blackened field",
    "stone tolls once for the forgotten heir",

    "fog gathers under the hanging bridge",
    "tower leans toward the darkened sea",
    "salt clings to the rusted armor",
    "city waits behind its hollow walls",
    "glass cracks beneath a patient footstep",
    "shadow follows without a name",
    "cloak drifts through the empty corridor",
    "thorn grows through the silver crown",
    "iron door trembles at midnight",
    "marsh swallows the echo of prayer",

    "gate opens only for the nameless",
    "flame flickers beneath the broken sigil",
    "wind erases the path behind the traveler",
    "wolf waits beside the silent well",
    "river stains the stone with memory",
    "banner falls into the waiting dust",
    "candle gutters before the final word",
    "map curls at the edges of truth",
    "spell fractures under its own weight",
    "cathedral sinks into the winter fog",

    "ashes settle on the wounded road",
    "lantern swings above the drowned stone",
    "crow lands where the blade once sang",
    "sea breathes against the shattered cliff",
    "thief listens for the turning lock",
    "grave opens under a careful hand",
    "stone arch frames the burning sky",
    "witch whispers to the sleeping roots",
    "moon leans close to the dying fire",
    "king walks alone beyond the gate",

    "bridge collapses into the dark water",
    "stone cracks during the final hymn",
    "forest tightens around the wandering knight",
    "frost blooms across the silent shield",
    "oath binds the wound of the city",
    "road trembles beneath distant thunder",
    "shadow folds into the ruined stair",
    "tower keeps watch over the broken plain",
    "river forgets the shape of its banks",
    "ember glows inside the hollow crown",

    # --- fable layer (softened, mythic) ---
    "beast kneels before the king and asks for mercy",
    "mercy is beaten until it learns silence",
    "hunter runs with two spears and no mercy",
    "agreement is stronger than bravery",
    "wheel breaks but the wheel remains",
    "three keys open different doors",
    "one enters one leaves one goes elsewhere",
    "seven sons named hunger famine fear plague murder betrayal land",
    "farmer buries thirst before fever speaks",
    "five eldest sons answer to tired hot cough thirst fever",
    "blind son sees only black",
    "eleventh name is never spoken twice",
    "season answers before the harvest",
    "oak tree measures time as nothing",
    "eternal things forget to count",

    # frogs stay
    "frog envies the dragonfly",
    "frog sinks because frogs do not fly",
    "frog watches the river without blinking",
    "frog waits where the river refuses",
    "frog listens to the stone without learning its name",
    "frog keeps still while the tower leans",
    "frog counts nothing and survives",
    
    # toned animal presences
    "hound outruns the lion and the lion outruns the man",
    "calf cannot eat what the mother names her own",
    "creature inherits that what was once buried",
    "it follows the trail of another creature",
    "he remembers what another beast would have forgot",
    "carries the mark of another creature",
    "moves where another once stood",
    "vermin scatter when the storm breaks",

    # --- abstraction counterweight ---
    "storm invents its own witness",
    "body learns the shape of silence",
    "absence gathers weight without sound",
    "memory leans against the final door",
    "time erases what it cannot carry",
    "breath enters and refuses to explain",
    "hunger names itself before the feast",
    "shadow becomes the only geography",
    "silence keeps what speech dissolves",
    "grief stands where the tower once stood",

    # --- relational / interior ---
    "you stood in the doorway and did not speak",
    "my hands remembered you before my mind did",
    "we slept back to back and called it peace",
    "your name broke softly against my teeth",
    "i was almost brave enough to stay",
    "you turned away and the room stayed warm",
    "i kept the cup you left on the table",
    "we mistook silence for safety",
    "your shadow moved before you did",
    "i learned your shape by leaving it",

    "i loved you in the hour before the storm arrived",
    "your absence kept speaking long after you were gone",
    "i asked for mercy and you offered truth instead",
    "we built a house from promises we never meant to keep",
    "my anger was only grief with sharper edges",
    "you held my face as if it might dissolve",
    "i learned your silence like a second language",
    "forgive me for the version of you i invented",
    "i stayed because leaving felt like treason",
    "we were gentle in ways that could not survive daylight",

    # --- other weathers: urban / liminal ---
    "rain collects in the broken fountain",
    "elevator opens onto a different floor",
    "candle burns behind the curtain",
    "staircase ends at a door that wasn't there",
    "the last train runs without passengers",
    "city breathes through its rusted vents",
    "voice rings out in an empty apartment",
    "lights flicker in the basement laundry",
    "pigeons gather where the market burned",
    "highway curls into the fog and doesn't return",

    # --- diner / waiting ---
    "stranger sits at the diner counter for years",
    "keeper knows his order but not his name",
    "tea cools in the same cup every morning",
    "music box plays the song she requested way back then",
    "the jar holds a single folded note",
    "kitchen closes but the fryer stays on",

    # --- domestic uncanny ---
    "glass breaks in the room upstairs",
    "no one lives upstairs",
    "floorboards remember footsteps that stopped",
    "mirror reflects a doorway that isn't there",
    "dust settles on the unwritten letter",

    # --- digital haunting ---
    "the machine shows you faces you used to know",
    "your ledger changes what is written when you're not looking",
    "every route leads back to a place you left",
    "tasks pile up like unopened messages",
    "you unravel the thread but the ghost remains",

    # --- residue / previous occupant ---
    "catalog arrives addressed to the previous tenant",
    "gardener tends roses planted by the dead",
    "box overflows with sympathy cards",
    "light burns out and no one replaces it",

    # --- construction / erasure ---
    "bones found under the construction site",
    "the new building is named for what it buried",
    "archaeologist cries in the alcove",
    "helmet covers a soft skull",
    "engine dreams of stopping",

    # --- institution / aftermath ---
    "bracelet still around the wrist",
    "papers list no fixed address",
    "machine accepts all the bad choices",
    "official hums a lullaby to the empty bed",
    "patron walks out and forgets to sign",

    # --- weather as memory ---
    "cloud forms the shape of your mother's disappointment",
    "wind carries the sound of a name you stopped using",
    "rain erases the trail back to yourself",
    "sunset bruises like an old argument",
    "dawn arrives with no apology",

    # --- waiting room ---
    "furniture bolted to the floor",
    "issues from three years ago",
    "officer calls a name no one claims",
    "clock ticks backward once an hour",
    "the door opens onto the same room",

    # --- child / absence ---
    "child draws a house with no doors",
    "teacher asks where the family goes",
    "child adds a window with no glass",
    "outside the frame, a figure waves",
    "figure has no face",

    # --- elemental refusal ---
    "river accepts everything and names nothing",
    "stone does not answer the question",
    "tree keeps count of the seasons it forgot",
    "mountain pretends not to notice you",
    "cave holds its breath until you leave",

    # --- first-person failure ---
    "i tried to write a letter but the ink turned to ash",
    "i tried to call but the line was busy with ghosts",
    "i tried to visit but the road kept folding",
    "i tried to forget but my hands remembered",
    "i tried to stay but the door had other plans",

    # --- promises that didn't hold ---
    "you said forever but meant until you got bored",
    "you left a key that doesn't fit any lock",
    "you sent a missive from a village that doesn't exist",
    "you signed your name in someone else's verse",
    
        # --- architectural / built spaces ---
    "the arch remembers every hand that touched it",
    "door frame holds the shape of those who passed through",
    "staircase turns back on itself and forgets the way down",
    "window looks out on a room that was never built",
    "column stands alone where the roof collapsed",
    "foundation settles into the earth like a body giving up",
    "corridor bends where no corner was drawn",
    "keystone waits for the weight it was meant to carry",
    "threshold worn smooth by feet that stopped coming",
    "atrium collects rain that falls through the missing dome",

    "wall breathes slowly with the settling of stones",
    "lintel bears the crack it was designed to hide",
    "basement fills with water that has nowhere else to go",
    "balcony overlooks a garden that forgot to grow",
    "pillar leans slightly, as if listening for something",
    "floorboards give slightly where someone always stood",
    "ceiling holds the echo of a voice that called too loud",
    "chapel pews face a window that only opens inward",
    "vestibule traps the cold between two doors",
    "attic holds the heat of every summer it survived",

    "bridge arch reflects in water that no longer flows",
    "pier reaches into the lake and finds nothing solid",
    "aqueduct carries only the memory of water",
    "cistern waits for rain that learned other routes",
    "well refuses to echo when you call into it",
    "tunnel curves so the end is never visible",
    "gate stands open but no one remembers why",
    "wall has a door that leads to more wall",
    "courtyard measures time by which stones are warm",
    "fountain collects coins for wishes no one made",

    "balustrade worn smooth where generations leaned",
    "pediment frames a sky that never finishes its sentence",
    "facade pretends the building still has insides",
    "portico offers shelter from weather that stopped coming",
    "colonnade counts the shadows between its columns",
    "rotunda turns slowly around its own emptiness",
    "apse faces east but the sun forgot the appointment",
    "nave holds silence like a body holds breath",
    "transept crosses itself and keeps going",
    "crypt does not distinguish between bones and dust",

    "eaves drip long after the rain has ended",
    "gable points at clouds that have no names",
    "dormer window watches the street with blind glass",
    "cornice catches light that will never enter",
    "spire aims at heaven but lost its sharpness",
    "buttress leans into a wall that no longer pushes back",
    "vault distributes weight that was never counted",
    "architrave frames a door that only opens in dreams",
    "plinth holds the absence of the statue it awaited",
    "capital flowers into stone leaves that never fell",

    "library keeps books that no one will open",
    "archive stores documents that describe lost buildings",
    "map room charts territories that drowned",
    "observatory turns toward stars that burned out",
    "scriptorium holds the silence after the last copy",
    "sacristy keeps vestments for rites no longer spoken",
    "cloister walks itself in the absence of feet",
    "chapter house convenes without members",
    "refectory tables wait for a feast that was never announced",
    "dormitory beds hold the shapes of those who did not return",
    
]
corpus_lines = set(corpus)

# ============================================================
# 2. COUNT MODELS: 4-GRAM + 3-GRAM + 2-GRAM (interpolated)
# ============================================================

fourgram_counts = defaultdict(Counter)
trigram_counts  = defaultdict(Counter)
bigram_counts   = defaultdict(Counter)

for line in corpus:
    toks = line.split()

    t4 = ["<START>"] * 3 + toks + ["<END>"]
    for i in range(len(t4) - 3):
        fourgram_counts[tuple(t4[i:i+3])][t4[i+3]] += 1

    t3 = ["<START>"] * 2 + toks + ["<END>"]
    for i in range(len(t3) - 2):
        trigram_counts[tuple(t3[i:i+2])][t3[i+2]] += 1

    t2 = ["<START>"] + toks + ["<END>"]
    for i in range(len(t2) - 1):
        bigram_counts[(t2[i],)][t2[i+1]] += 1


def _dist_from_counts(counter, temperature=0.9, top_k=8):
    if not counter:
        return None
    items = sorted(counter.items(), key=lambda x: x[1], reverse=True)[:top_k]
    words, freqs = zip(*items)
    freqs = [f ** (1.0 / temperature) for f in freqs]
    total = sum(freqs)
    probs = [f / total for f in freqs]
    return words, probs


def sample_ngram_interpolated(ctx4, line_mode, temperature=0.9, top_k=8,
                              w4=0.6, w3=0.3, w2=0.1):
    d4 = _dist_from_counts(fourgram_counts.get(ctx4), temperature, top_k)
    ctx3 = (ctx4[1], ctx4[2])
    d3 = _dist_from_counts(trigram_counts.get(ctx3), temperature, top_k)
    ctx2 = (ctx4[2],)
    d2 = _dist_from_counts(bigram_counts.get(ctx2), temperature, top_k)

    prob_map = defaultdict(float)
    if d4:
        words, probs = d4
        for w, p in zip(words, probs):
            prob_map[w] += w4 * p
    if d3:
        words, probs = d3
        for w, p in zip(words, probs):
            prob_map[w] += w3 * p
    if d2:
        words, probs = d2
        for w, p in zip(words, probs):
            prob_map[w] += w2 * p

    if not prob_map:
        return "<END>"

    # register bias (kept)
    rel_tokens = {"i","you","we","my","your","our","me","us"}
    strength = 0.22  # was 0.55

    for w in list(prob_map.keys()):
        if w in ("<START>", "<END>"):
            continue
        if w in rel_tokens:
            if line_mode == "relational":
                prob_map[w] *= (1.0 + strength)
            else:
                prob_map[w] *= (1.0 - 0.60 * strength)  # damp pronouns harder in myth
        else:
            if line_mode == "myth":
                prob_map[w] *= 1.01

    words = list(prob_map.keys())
    probs = np.array([prob_map[w] for w in words], dtype=float)
    probs /= probs.sum()
    return random.choices(words, weights=probs, k=1)[0]


# ============================================================
# 3. NEURAL TRIGRAM (tiny MLP)
# ============================================================

vocab = sorted(set(word for line in corpus for word in line.split()))
vocab = ["<START>", "<END>"] + vocab
v2i = {w: i for i, w in enumerate(vocab)}
i2v = {i: w for w, i in v2i.items()}
V = len(vocab)

dim = 32
hidden = 64

E  = np.random.randn(V, dim) * 0.1
W1 = np.random.randn(dim * 2, hidden) * 0.1
b1 = np.zeros(hidden)
W2 = np.random.randn(hidden, V) * 0.1
b2 = np.zeros(V)

trigrams = []
for line in corpus:
    tokens = ["<START>"] + line.split() + ["<END>"]
    for i in range(len(tokens) - 2):
        trigrams.append((tokens[i], tokens[i+1], tokens[i+2]))

lr = 0.05
neural_epochs = 9
for _ in range(neural_epochs):
    random.shuffle(trigrams)
    for w1, w2, w3 in trigrams:
        i1, i2, i3 = v2i[w1], v2i[w2], v2i[w3]
        x = np.concatenate([E[i1], E[i2]])
        h = np.tanh(x @ W1 + b1)
        logits = h @ W2 + b2
        logits -= np.max(logits)
        probs = np.exp(logits); probs /= probs.sum()

        dlogits = probs
        dlogits[i3] -= 1

        dW2 = np.outer(h, dlogits)
        db2 = dlogits

        dh = dlogits @ W2.T
        dh_raw = dh * (1 - h**2)

        dW1 = np.outer(x, dh_raw)
        db1 = dh_raw

        dx = dh_raw @ W1.T
        dE1, dE2 = np.split(dx, 2)

        W2 -= lr * dW2; b2 -= lr * db2
        W1 -= lr * dW1; b1 -= lr * db1
        E[i1] -= lr * dE1; E[i2] -= lr * dE2


# ============================================================
# 4. GUARDS + SHAPING + REGISTER
# ============================================================

function_words = {
    "a","the","and","or","but","if","at","in","on","of","is","are","was","were",
    "to","for","from","about","during","with"
}

bad_endings = {"of","in","to","with","about","during","and","or","the"}

rel_tokens = {"i","you","we","my","your","our","me","us"}

def choose_stanza_plan():
    plans = [
        ["myth", "myth", "myth"],
        ["myth", "myth", "myth"],       # duplicate to bias further
        ["myth", "relational", "myth"],
        ["myth", "myth", "relational"],
        ["relational", "myth", "myth"],
    ]
    weights = [0.46, 0.10, 0.24, 0.14, 0.06]
    return random.choices(plans, weights=weights, k=1)[0]

# --- corpus chunk guard (6-grams) ---
corpus_6grams = set()
for line in corpus:
    w = line.split()
    if len(w) >= 6:
        for i in range(len(w) - 5):
            corpus_6grams.add(" ".join(w[i:i+6]))

def contains_corpus_chunk(tokens, n=6):
    raw = [t.rstrip(",") for t in tokens]
    if len(raw) < n:
        return False
    for i in range(len(raw) - n + 1):
        if " ".join(raw[i:i+n]) in corpus_6grams:
            return True
    return False

def has_relational_markers(tokens):
    raw = [t.rstrip(",") for t in tokens]
    return any(w in rel_tokens for w in raw)

def choose_stance_and_anchor():
    idxs = random.sample(range(V), 3)
    stance = np.mean([E[i] for i in idxs], axis=0)
    anchor = random.choice(vocab[2:])
    return stance, anchor

def is_verbish(w):
    w = w.rstrip(",")
    return w.endswith("s") or w.endswith("ed") or w.endswith("ing")

def violates_agreement(prev, nxt):
    prev = prev.rstrip(",")
    nxt  = nxt.rstrip(",")
    if prev in function_words:
        return False
    # cheap plural noun heuristic: discourage singular verbs after plural-ish nouns
    if prev.endswith("s") and len(prev) > 3:
        if nxt.endswith("s") and not nxt.endswith("ss"):
            return True
    return False

def prune(tokens):
    cleaned = []
    verb_streak = 0
    for w in tokens:
        ww = w.rstrip(",")
        if ww.endswith("s"):
            verb_streak += 1
            if verb_streak >= 3:
                continue
        else:
            verb_streak = 0
        cleaned.append(w)
    return cleaned

def light_hygiene(tokens):
    cleaned = []
    for w in tokens:
        wr = w.rstrip(",")
        if cleaned and cleaned[-1].rstrip(",") == wr:
            continue
        if cleaned and (cleaned[-1].rstrip(",") in function_words) and (wr in function_words):
            continue
        cleaned.append(w)

    # strip edges (but don't strip if edge is relational)
    if cleaned and cleaned[0].rstrip(",") in function_words and cleaned[0].rstrip(",") not in rel_tokens:
        cleaned = cleaned[1:]
    if cleaned and cleaned[-1].rstrip(",") in function_words and cleaned[-1].rstrip(",") not in rel_tokens:
        cleaned = cleaned[:-1]
    return cleaned

def punctuate(tokens):
    raw = [t.rstrip(",") for t in tokens]
    if len(tokens) < 9:
        return tokens

    candidates = list(range(2, len(tokens) - 2))
    random.shuffle(candidates)
    for i in candidates:
        wi = raw[i]
        if wi in function_words:
            continue
        if tokens[i].endswith(","):
            continue
        if is_verbish(wi) and random.random() < 0.6:
            continue
        tokens[i] = tokens[i] + ","
        break
    return tokens

def repair(tokens):
    if not tokens:
        return tokens

    out = []
    i = 0
    while i < len(tokens):
        w = tokens[i]
        wr = w.rstrip(",")

        if w.endswith(",") and wr in function_words:
            w = wr

        # drop token after 'of' if function or verbish (unless relational)
        if out and out[-1].rstrip(",") == "of":
            if (wr in function_words or is_verbish(wr)) and wr not in rel_tokens:
                i += 1
                continue

        # drop "beside" after function-ish anchors
        if out:
            prev = out[-1].rstrip(",")
            if wr == "beside" and prev in {"the","only","was","were","is","are","to","for","from","in","on","of"}:
                i += 1
                continue

        out.append(w)
        i += 1

    while out and out[-1].rstrip(",") in function_words and out[-1].rstrip(",") not in rel_tokens:
        out.pop()
    while out and out[0].rstrip(",") in function_words and out[0].rstrip(",") not in rel_tokens:
        out = out[1:]

    return out


# ============================================================
# 5. REGISTER-AWARE NEURAL SAMPLING (KeyError fix kept)
# ============================================================

def sample_neural(w1, w2, stance_vec, line_mode, temperature=0.8):
    i1, i2 = v2i[w1], v2i[w2]
    x = np.concatenate([E[i1], E[i2]])
    h = np.tanh(x @ W1 + b1)
    logits = (h @ W2 + b2) / temperature

    # stance bias
    sims = np.array([np.dot(E[i], stance_vec) for i in range(V)])
    logits += 0.15 * sims

    # register bias (guard membership)
    bias = np.zeros(V, dtype=float)
    for tok in rel_tokens:
        if tok in v2i:
            bias[v2i[tok]] = 1.0

    if line_mode == "relational":
        logits += 0.18 * bias    
    else:
        logits -= 0.28 * bias     
        
    logits -= np.max(logits)
    probs = np.exp(logits); probs /= probs.sum()
    idx = np.random.choice(range(V), p=probs)
    return i2v[idx]


# ============================================================
# 6. GENERATION (hybrid burst + taper + agreement + min length)
# ============================================================

def generate_line(stance_vec, line_mode, anchor_word=None, prefer_mode=None):
    tokens = []
    ctx4 = ("<START>", "<START>", "<START>")
    ctx2 = ("<START>", "<START>")

    mode = prefer_mode if prefer_mode else random.choice(["4gram", "neural"])
    burst = random.randint(1, 6)

    target_len = random.randint(9, 17) if line_mode == "relational" else random.randint(10, 18)

    for step in range(target_len):
        # taper: final 3 steps use n-gram for concreteness
        if (target_len - step) <= 3:
            mode = "4gram"

        if burst <= 0:
            if tokens and tokens[-1].rstrip(",") in function_words:
                burst = 1
            else:
                mode = random.choice(["4gram", "neural"])
                burst = random.randint(1, 6)

        if mode == "4gram":
            nxt = sample_ngram_interpolated(ctx4, line_mode, temperature=0.9, top_k=8)
        else:
            nxt = sample_neural(ctx2[0], ctx2[1], stance_vec, line_mode)

        burst -= 1
        if nxt in ("<END>", "<START>"):
            break

        # agreement guard (one retry)
        if tokens and violates_agreement(tokens[-1], nxt):
            if mode == "4gram":
                alt = sample_ngram_interpolated(ctx4, line_mode, temperature=0.9, top_k=8)
            else:
                alt = sample_neural(ctx2[0], ctx2[1], stance_vec, line_mode)

            if alt not in ("<END>", "<START>") and not violates_agreement(tokens[-1], alt):
                nxt = alt

        # IMPORTANT: append token (this is the silent-murder bug in some versions)
        tokens.append(nxt)

        # update contexts
        ctx4 = (ctx4[1], ctx4[2], nxt)
        ctx2 = (ctx2[1], nxt)

    # shaping pipeline (restored)
    tokens = prune(tokens)
    tokens = light_hygiene(tokens)
    tokens = repair(tokens)
    tokens = punctuate(tokens)
    tokens = repair(tokens)

    # anchor injection (gentle, skip sometimes on relational)
    raw = [t.rstrip(",") for t in tokens]
    if anchor_word and anchor_word not in raw:
        if line_mode == "relational" and random.random() < 0.55:
            pass
        else:
            tokens.insert(max(0, len(tokens) - 2), anchor_word)

    return tokens


# ============================================================
# 7. SCORING (ending discipline + repetition dampener + rails)
# ============================================================

def score_line(raw, line_mode, anchor_word):
    if not raw:
        return -999.0

    score = 0.0
    score += len(set(raw))

    # length sanity
    if line_mode == "relational":
        if len(raw) < 7:
            score -= 2.5
    else:
        if len(raw) < 8:
            score -= 3.0
    if len(raw) > 18:
        score -= 1.0

    # ending discipline
    end = raw[-1]
    if end and end not in function_words:
        score += 0.8
    if end in bad_endings:
        score -= 1.2

    # anchor reward
    if anchor_word in raw:
        score += 0.7 if line_mode == "myth" else 0.45

    # function density penalty
    fw = sum(1 for w in raw if w in function_words)
    score -= max(0.0, fw - (len(raw) * 0.45)) * 0.6

    # register sanity
    if line_mode == "relational":
        if not any(w in rel_tokens for w in raw):
            score -= 1.4
    else:
        pron = sum(1 for w in raw if w in rel_tokens)
        if pron >= 2:
            score -= (pron - 1) * 1.25   # was >=3 and gentler

    return score


def score_stanza(lines_as_tokens, modes, anchor_word, used_lines):
    score = 0.0
    stanza_tokens = []

    joined = [" ".join(l) for l in lines_as_tokens]

    # rail suppression: penalize repeating any full output line within the run
    for j in joined:
        if j in used_lines:
            score -= 3.5

    for lt, mode in zip(lines_as_tokens, modes):
        raw = [w.rstrip(",") for w in lt]
        stanza_tokens.extend(raw)
        score += score_line(raw, mode, anchor_word)
        
    # pronoun inertia penalty: punish clumps like "you ... my ... you ... my ..."
    inertia = 0
    run = 0
    for w in stanza_tokens:
        if w in rel_tokens:
            run += 1
            if run >= 2:
                inertia += (run - 1)
        else:
            run = 0
    score -= 0.55 * inertia

    # repetition dampener (pronouns get partial immunity)
    counts = Counter(stanza_tokens)
    for word, count in counts.items():
        if count >= 3:
            if word in rel_tokens:
                score -= (count - 3) * 0.35
            else:
                score -= (count - 2) * 1.05
                
    # cap relational saturation            
    rel_count = sum(1 for w in stanza_tokens if w in rel_tokens)
    if rel_count > 6:
        score -= (rel_count - 6) * 0.8
    
    # encourage frame-cut-frame coherence
    if modes == ["myth", "relational", "myth"]:
        score += 0.9

    return score


def enforce_min_line(tokens, line_mode):
    # hard guard against the “single token” collapse
    raw = [t.rstrip(",") for t in tokens]
    min_len = 7 if line_mode == "relational" else 8
    return len(raw) >= min_len


def generate_stanza(used_lines):
    best = None
    best_score = -1e9

    modes = choose_stanza_plan()

    for _ in range(12):  # more candidates = fewer "generation failed" and less rail-lock
        stance_vec, anchor = choose_stance_and_anchor()

        l1 = generate_line(stance_vec, modes[0], anchor_word=anchor, prefer_mode="4gram")
        l2 = generate_line(stance_vec, modes[1], anchor_word=None,   prefer_mode=None)
        l3 = generate_line(stance_vec, modes[2], anchor_word=anchor, prefer_mode="neural")

        # min length enforcement (regen once if needed)
        for idx, (lt, mode) in enumerate([(l1, modes[0]), (l2, modes[1]), (l3, modes[2])]):
            if not enforce_min_line(lt, mode):
                # one retry, slightly longer target pressure via re-call
                if idx == 0:
                    l1 = generate_line(stance_vec, modes[0], anchor_word=anchor, prefer_mode="4gram")
                elif idx == 1:
                    l2 = generate_line(stance_vec, modes[1], anchor_word=None, prefer_mode=None)
                else:
                    l3 = generate_line(stance_vec, modes[2], anchor_word=anchor, prefer_mode="neural")

        lines = [l1, l2, l3]
        joined = [" ".join(l) for l in lines]

        # reject exact corpus lines
        if any(j in corpus_lines for j in joined):
            continue

        # chunk guard: strong on myth lines, lighter on relational
        ok = True
        for lt, mode in zip(lines, modes):
            if mode == "myth":
                if contains_corpus_chunk(lt, n=6):
                    ok = False; break
            else:
                if contains_corpus_chunk(lt, n=6) and not has_relational_markers(lt):
                    ok = False; break
        if not ok:
            continue

        s = score_stanza(lines, modes, anchor, used_lines)
        if s > best_score:
            best_score = s
            best = joined

    if not best:
        return "(generation failed)"

    # register "used lines" so we don't rail-repeat within a run
    for j in best:
        used_lines.add(j)

    return "\n".join(best)


# ============================================================
# 8. RUN
# ============================================================

print("\n=== Hybrid Authorial Engine v11.11 (Stabilizers + Encoding + Rail Control) ===\n")

used_lines = set()
for _ in range(5):
    print(generate_stanza(used_lines))
    print()