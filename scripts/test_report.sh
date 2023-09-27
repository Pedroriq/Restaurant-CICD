echo "Instalando pacote mailutils"
sudo apt-get install mailutils
echo "Fim da instalacao"
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest --html=report.html
mkdir test
mv report.html assets test/
zip -r test.zip test/
cat test.zip | mail -s "Test_Report_Restaurant" ${EMAIL_LIST} -A test.zip
echo "Email enviado"