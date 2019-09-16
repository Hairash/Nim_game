program nim_bot;
var
  f_res, f_pos: text;
  a, b, c, idx, val: integer;

begin
  writeln('slow bot');
  assign(f_pos, 'position.txt');
  reset(f_pos);
  read(f_pos, a, b, c);
  close(f_pos);
  
  if a > 0 then
    idx := 1
  else if b > 0 then
    idx := 2
  else
    idx := 3;
  val := 1;
  
  sleep(10000);
  writeln('is so slow');

  assign(f_res, 'result.txt');
  rewrite(f_res);
  write(f_res, idx, ' ', val);
  close(f_res);
end.