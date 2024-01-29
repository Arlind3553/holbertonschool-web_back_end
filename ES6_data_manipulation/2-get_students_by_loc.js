export default function getStudentsByLocation (list, city) {
  return list.filter((cities) => cities.location === city);
}
