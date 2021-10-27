
current_dir=$PWD
cd ..
git clone $1 && cd "$(basename "$_" .git)"
sudo cp -R  $current_dir/ $PWD/
git checkout -b $2
git add .
git commit -m "First Commit"
git push origin $2