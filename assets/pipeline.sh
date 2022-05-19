#!/bin/bash
echo "(0) Preparing pipeline"
if [ $# -eq 0 ]; then
    echo "Error: Please provide a custom commit message"
    exit
fi

echo "(1) Build (compiling the application)"
npm install
if npm run build; then 
    echo "Build Succeeded"
else
    echo "Build Failed"
    exit
fi
#echo "(2) Test"

echo "(3) Release (comitting to a repo)"
git add .
git commit -m "$1"
git push origin main

echo "(4) Deploy (deployed to production)"
npm run start
