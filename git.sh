
current_dir=$PWD
cd ..
git clone https://github.com/atulnitkkr/Music-Player.git && cd "$(basename "$_" .git)"
sudo cp -R  $current_dir/ $PWD/
git checkout -b asdf
git add .
git commit -m "First Commit"
git push origin asdf