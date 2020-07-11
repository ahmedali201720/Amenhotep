import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'block',
  pure: false,
})
export class BlockPipe implements PipeTransform {
  transform(value: any, filter: number): any {
    console.log(value);
    const blockArray: any[] = [];
    for (let i = 0; i < value.length; i++) {
      console.log(value[i]);
      let compoundNum: number = value[i].compound;
      if (compoundNum === filter) {
        blockArray.push(value[i]);
      }
    }
    return blockArray;
  }
}
