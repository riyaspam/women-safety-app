# audio_processing.py


BASE = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE, 'model')
CLASSIFIER_PATH = os.path.join(MODEL_DIR, 'audio_classifier.pkl')
LABELS_PATH = os.path.join(MODEL_DIR, 'label_names.npy')


# Load classifier if exists
_classifier = None
_labels = None
_processor = None
_wav2vec = None


def _lazy_load():
global _classifier, _labels, _processor, _wav2vec
if _classifier is None:
if os.path.exists(CLASSIFIER_PATH):
_classifier = joblib.load(CLASSIFIER_PATH)
if os.path.exists(LABELS_PATH):
_labels = np.load(LABELS_PATH, allow_pickle=True).tolist()
# load wav2vec processor & model (CPU safe)
try:
_processor = Wav2Vec2Processor.from_pretrained('facebook/wav2vec2-base-960h')
_wav2vec = Wav2Vec2Model.from_pretrained('facebook/wav2vec2-base-960h')
_wav2vec.eval()
except Exception:
_processor = None
_wav2vec = None


def extract_embedding(path, sr=16000):
y, orig_sr = librosa.load(path, sr=sr, mono=True)
if _processor is None or _wav2vec is None:
raise RuntimeError('Wav2Vec not loaded')
inputs = _processor(y, sampling_rate=sr, return_tensors='pt', padding=True)
with torch.no_grad():
outputs = _wav2vec(inputs.input_values).last_hidden_state
emb = outputs.mean(dim=1).squeeze().numpy()
return emb




def predict_from_file(path):
_lazy_load()
if _labels is None or _classifier is None:
# fallback: simple energy-based heuristic
y, sr = librosa.load(path, sr=16000)
energy = np.mean(np.abs(y))
if energy > 0.02:
return 'possible_event', 0.5
return 'normal', 0.2


emb = extract_embedding(path)
probs = None
try:
probs = _classifier.predict_proba([emb])[0]
except Exception:
pred = _classifier.predict([emb])[0]
label = _labels[int(pred)] if _labels else str(pred)
return label, 1.0
pred_idx = int(np.argmax(probs))
score = float(probs[pred_idx])
label = _labels[pred_idx] if _labels else str(pred_idx)
return label, score
