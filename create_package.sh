uv init .      
uv sync
mkdocs new .
cp ../tools/run_build.sh .
cp ../tools/run_test.sh .
cp ../tools/update_docs.sh .
bash update_docs.sh 