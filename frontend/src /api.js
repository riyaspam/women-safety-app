const API = "http://127.0.0.1:5000";

export const registerUser = async (data) => {
  const res = await fetch(`${API}/api/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
};

export const loginUser = async (data) => {
  const res = await fetch(`${API}/api/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
};

export const uploadAudio = async (file) => {
  const form = new FormData();
  form.append("file", file);

  const res = await fetch(`${API}/api/predict_audio`, {
    method: "POST",
    body: form,
  });

  return res.json();
};

export const saveLocation = async (payload) => {
  const res = await fetch(`${API}/api/update_location`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  return res.json();
};
