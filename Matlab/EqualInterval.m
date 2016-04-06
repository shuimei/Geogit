function [ei,hist_ei]=EqualInterval(x, num)
    Min=min(min(x));
    Max=max(max(x));
    range=Min:(Max-Min)/(num-1):Max;
    ei=zeros(size(x));
    for i=1:length(range)-1
        ei(x>=range(i))=i;
    end
    hist_ei=hist(ei,range);
end