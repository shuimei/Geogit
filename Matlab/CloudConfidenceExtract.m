filePath='E:\Data\Washington\cloudQF1Clip';
fileList=dir(fullfile(filePath,'*.tif'));
outPath='E:\Data\Washington\cloudResult';
i=1;
n=length(fileList);
while(i<=n)
    inFile=strcat(filePath,'\',fileList(i).name);
    outFile=strcat(outPath,'\CloudConfidence\',fileList(i).name);
    [I,R]=geotiffread(inFile);
    [r,c]=size(I);
    lineI=reshape(I,[c*r,1]);
    bI=dec2bin(lineI,8);
    %cloud confidence
    lineCloudConfi=bin2dec(bI(:,5:6));
    %night0,day1
    lineDayOrNight=bin2dec(bI(:,4));
    %cloud test performed
    lineTestPfm=bin2dec(bI(:,7:8));
    
    cloudConfi=reshape(lineCloudConfi,[r,c]);
    testPfm=reshape(lineTestPfm,[r,c]);
    
    info=geotiffinfo(inFile);
    if(exist(outFile)==2)
        delete(outFile);
    end
    
    geotiffwrite(outFile,cloudConfi,R,'GeoKeyDirectoryTag', info.GeoTIFFTags.GeoKeyDirectoryTag);
    %C = arrayfun(@(x)dec2bin(x,8),I,'UniformOutput',false);
    
    i=i+1
end
    

