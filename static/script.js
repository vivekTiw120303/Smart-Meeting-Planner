async function sendSlots() {
  const data = document.getElementById("jsonInput").value;
  const response = await fetch("/slots", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: data
  });
  alert("Slots submitted!");
}

async function getSuggestions() {
  const duration = document.getElementById("duration").value;
  const response = await fetch(`/suggest?duration=${duration}`);
  const slots = await response.json();

  const table = document.getElementById("resultsTable");
  table.innerHTML = "<tr><th>Start</th><th>End</th></tr>";

  slots.forEach(([start, end]) => {
    const row = table.insertRow();
    row.insertCell(0).innerText = start;
    row.insertCell(1).innerText = end;
  });
}