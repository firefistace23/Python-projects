function hello ()
{
  echo "sum is $(($1+$2))"
}
echo "enter  2 nos :"
read a b
hello a b
