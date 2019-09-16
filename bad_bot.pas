program nim_bot;
var
  f_res, f_pos: text;
  a, b, c, idx, val: integer;

begin
  write('bot 2');
  assign(f_pos, 'position.txt');
  reset(f_pos);
  read(f_pos, a, b, c);
  close(f_pos);
  
  idx := random(3) + 1;
  val := random(5) + 1;

  assign(f_res, 'result.txt');
  rewrite(f_res);
  write(f_res, idx, ' ', val);
  close(f_res);  
end.