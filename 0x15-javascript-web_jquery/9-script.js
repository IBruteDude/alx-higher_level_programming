async function changeData () {
  const response = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
  let data = await response.json();
  data = data.hello;
  document.querySelector('DIV#hello').textContent = data;
}
changeData();
