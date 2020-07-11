import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'flat',
})
export class FlatPipe implements PipeTransform {
  transform(value: any, tid: number): any {
    console.log(value);
    const flatArray: any[] = [];
    for (let i = 0; i < value.length; i++) {
      console.log(value[i]);
      let towerNum: number = value[i].tower;
      if (towerNum === tid) {
        flatArray.push(value[i]);
      }
    }
    return flatArray;
  }
}
