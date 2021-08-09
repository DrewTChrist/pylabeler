UIDIR="ui/*"
PYDIR="pylabeler/"
PYEXT='.py'

for F in $UIDIR
do
	NAME=$(echo $F | cut -d'.' -f 1)
	pyuic5 $F -o "$PYDIR$NAME$PYEXT"
done
