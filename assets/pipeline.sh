#echo "(0) Preparing pipeline"

echo "(1) Build (compiling the application)"
npm install
if npm run build; then 
    echo "Build Succeeded"
else
    echo "Build Failed"
    exit
fi
git add .
git commit -m "COMPX341-22A-A3 Commiting from CI/CD Pipeline"
git push origin master

npm run start

#echo "(2) Test"

#echo "(3) Release (comitting to a repo)"

#echo "(4) Deploy (deployed to production)"