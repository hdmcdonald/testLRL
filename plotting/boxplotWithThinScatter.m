function boxplotWithThinScatter(YA_OA,dataTable,dataIndex,opts)
% boxplot([dataTable{YA_OA==0,dataIndex};dataTable{YA_OA==1,dataIndex}],YA_OA,'colors','k'); hold on;
% customBoxPlotHDC(dataTable{YA_OA==0,dataIndex}, opts)
optsOrig = opts;
xPos1 = opts.xPos;
opts.barColor = optsOrig.barColor(1,:);
hold on
customBoxPlotHDC(dataTable{YA_OA==0,dataIndex}, opts)
opts.xPos = opts.xPos + opts.barSpace;
opts.barColor = optsOrig.barColor(2,:);
customBoxPlotHDC(dataTable{YA_OA==1,dataIndex}, opts)
xPos2 = opts.xPos;

G = xPos1.*~YA_OA + xPos2.*YA_OA;
c = [[0.9:-0.2:0.1]'.*ones(5,3); 0 0 0];        % define a gray color gradient
xShift = opts.xShift;
if size(dataTable,2) > 1
for iLevel = 2:size(dataTable,2)
    swarmchart([G+xShift], dataTable{:,iLevel},15,c(iLevel-1,:),'filled','XJitter',opts.JitterOpt,'XJitterWidth',opts.JitterWidth, 'MarkerFaceAlpha',0.5)
    xShift = xShift + 0.05;
end
clear iLevel
else
    swarmchart(G, dataTable{:,1},20,c(4,:),'filled','XJitter',opts.JitterOpt,'XJitterWidth',opts.JitterWidth, 'MarkerFaceAlpha',0.6)
end
% title(titleString)
% ylabel(ylabelString)
end