for i in *; do
  if [[ $(du -h "$i" | awk '{print $1}') = 0 ]]; then
    echo "$i is empty."
fi
done
