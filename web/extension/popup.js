document.getElementById('verify-btn').addEventListener('click', async () => {
  const intent = document.getElementById('intent').value;
  const evidence = document.getElementById('evidence').value;
  const resultPre = document.getElementById('result');

  resultPre.textContent = 'Verifying with Ω∞v VaaS...';

  try {
    const res = await fetch('http://localhost:8000/api/vaas/verify', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ intent, evidence, target: 'javascript' }),
    });

    const data = await res.json();
    resultPre.textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    resultPre.textContent = 'Error connecting to http://localhost:8000: ' + err.message;
  }
});
