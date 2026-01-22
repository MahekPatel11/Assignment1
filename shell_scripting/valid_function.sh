check_length() {
  if [ ${#1} -ge 5 ]; then
    echo "Input length is valid"
  else
    echo "Input too short"
  fi
}

check_length "$1"