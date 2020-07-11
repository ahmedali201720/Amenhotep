import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'tower',
})
export class TowerPipe implements PipeTransform {
  transform(value: any, bid: number): any {
    console.log(value);
    const towerArray: any[] = [];
    for (let i = 0; i < value.length; i++) {
      console.log(value[i]);
      let blockNum: number = value[i].block;
      if (blockNum === bid) {
        towerArray.push(value[i]);
      }
    }
    return towerArray;
  }
}
