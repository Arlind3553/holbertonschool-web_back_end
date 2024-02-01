export default function cleanSet(set, startString) {
    if (typeof startString !== 'string') {
    return '';
    }
    const filteredValues = Array.from(set).filter(value => value.startsWith(startString));
    const resultString = filteredValues.map(value => value.slice(startString.length)).join('-');
    if (startString == '') {
        return '';
    }
    return resultString;
}
