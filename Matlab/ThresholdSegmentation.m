function [threshold_matrix]=ThresholdSegmentation(x,thr)
    threshold_matrix=x;
    threshold_matrix(x<=thr)=0;
    threshold_matrix(x>thr)=1;
end