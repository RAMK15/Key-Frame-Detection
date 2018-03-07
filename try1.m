vid = 'Wildlife 00_00_20-00_00_30.avi';
readerobj = mmreader(vid);
for k=1:readerobj.NumberOfFrames
    I=read(readerobj,k);
    if(k~= readerobj.NumberOfFrames)
        J=read(readerobj,k+1);
        sss=absdif(I,J);
        X(k)=sss;
    end
end
mean=mean2(X)
std=std2(X)
threshold=std+mean*4
for k=1: readerobj.NumberOfFrames
    I =  read(readerobj,k);
    if(k~=readerobj.NumberOfFrames)
        J=read(readerobj,k+1);
        sss=absdif(I,J);
        if(sss>mean)
            imwrite(J,strcat('D:\',Names{k+1}));
        end
    end
end