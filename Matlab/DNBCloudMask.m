function [DNB, CC, CC1, CC2, CC3] = DNBCloudMask(workspace1, workspace2, dnbname, ccname)
    cd(workspace1);
    [DNB R] = geotiffread(dnbname);
    cd(workspace2);
    [CC J] = geotiffread(ccname);
    CC1=zeros(size(CC));
    CC2=zeros(size(CC));
    CC3=zeros(size(CC));
end