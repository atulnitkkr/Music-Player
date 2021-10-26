
current_dir=$PWD
cd ..
git clone https://github.com/atulnitkkr/Music-Player.git && cd "$(basename "$_" .git)"
cp -R  $current_dir/ $PWD/
git checkout -b efg
git add .
git commit -m "First Commit"
git push origin efg