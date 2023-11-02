$('header').attr('style', (index, oldcontent) => {
  if (oldcontent === 'color: #FF0000') return oldcontent;
  else if (oldcontent === undefined) return 'color: #FF0000';
  return oldcontent + '; color: #FF0000';
});
