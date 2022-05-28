
# rename files via ${PREFIX}
prefix=BKJN_; files=$(find *.py); echo $files; for file in $files; do mv $file ${prefix}${file}; done
