async function sankeyfier(url) {
    const response = await fetch(url);
    const csvData = await response.text();

    const lines = csvData.split('\n');
    const labelSet = new Set();
    const labelMap = new Map();

    const source = [];
    const target = [];
    const value = [];

    lines.forEach(line => {
        const [sourceStr, targetStr, valueStr] = line.split(',');
        if (sourceStr && targetStr && valueStr) {
            if (!labelSet.has(sourceStr)) {
                const index = labelSet.size;
                labelSet.add(sourceStr);
                labelMap.set(sourceStr, index);
            }
            if (!labelSet.has(targetStr)) {
                const index = labelSet.size;
                labelSet.add(targetStr);
                labelMap.set(targetStr, index);
            }

            source.push(labelMap.get(sourceStr));
            target.push(labelMap.get(targetStr));
            value.push(parseInt(valueStr));
        }
    });

    const label = Array.from(labelSet);

    return {
        label,
        source,
        target,
        value
    };
}