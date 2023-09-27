echo "Instalando pacote mailutils"
sudo apt-get install mailutils
echo "Fim da instalacao"
echo "Build successful" | mail -s "Test_Report_Restaurant" ${EMAIL_LIST}
echo "Email enviado"