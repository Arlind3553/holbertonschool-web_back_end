export default function getStudentIdsSum(list) {
  return list.reduce((shuma, student) => shuma + student.id, 0);
}
