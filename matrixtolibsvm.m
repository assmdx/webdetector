function svmtransform(A)
[m,n]=size(A);
fid = fopen('A.txt','w');%д���ļ�·��
for i=1:m
temp1 = A(i,2:n);%�洢A��ÿһ�дӵ�2λ��ʼ��ֵ
temp2 = [];
for j = 1:length(temp1)
if temp1(j) ~= 0
temp2 = [temp2 ' ' num2str(j) ':' num2str(temp1(j))];
else
temp2 = [temp2 ' ' ' ' ' ' ' '];
end
end   % temp2���Aһ�������ŵĽ��
temp3 = [num2str(A(i,1)) temp2];%temp3�������һ�еĽ��
[m1 n1] = size(temp3);
for k = 1:n1
if k == n1
fprintf(fid,'%c\n',temp3(k));
else
fprintf(fid,'%c\t',temp3(k));
end
end
fclose(fid);
end
