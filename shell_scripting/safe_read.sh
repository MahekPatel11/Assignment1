set -u

filename="$1"

if [ ! -e "$filename" ]; then
  echo "Error: $filename does not exist"
  exit 1
fi

echo "Reading file contents:"
cat "$filename"
