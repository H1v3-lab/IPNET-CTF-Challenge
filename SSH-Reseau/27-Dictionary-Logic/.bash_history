ssh analyst@10.10.10.23
cat /var/log/auth.log | tail -n 20
grep -Rin 'password' ~/.ssh ~/.bash_history /var/log 2>/dev/null
sudo -l
echo 'IPNET{dictionary_osint_win}' 
exit
