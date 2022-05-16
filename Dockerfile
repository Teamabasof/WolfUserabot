# FROM kısmını Değiştirmeyiniz Owenye DockerFile Kullanın

FROM erdembey/epicuserbot:latest
RUN git clone https://github.com/Teamabasof/WolfUserabot /root/WolfUserabot
WORKDIR /root/WolfUserabot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]  
