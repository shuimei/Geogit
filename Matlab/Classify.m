function M = Classify(inM, interval)
    M = zeros(size(inM));
    for i = 1:length(interval)
        if i == 1
            M(inM < interval(i)) = i;
        elseif i <= length(interval)
            M(inM < interval(i) & inM >= interval(i - 1)) = i;
            M(inM >= interval(i)) = i+1;
        end
    end
end