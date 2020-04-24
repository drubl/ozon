import {Component, OnInit, Output, EventEmitter, ViewChild, ElementRef} from '@angular/core';
import {Observable, Subject, Subscription} from 'rxjs';


@Component({
  selector: 'app-search-form',
  templateUrl: './search-form.component.html',
  styleUrls: ['./search-form.component.css']
})
export class SearchFormComponent {
  @Output() onClickSearchSubmit: EventEmitter<string> = new EventEmitter<string>();
  @ViewChild('searchBox', {static: false}) searchBoxRef: ElementRef;
  @ViewChild('formSearch', {static: false}) formSearchRef: ElementRef;
  @ViewChild('buttonSearch', {static: false}) buttonSearchRef: ElementRef;

  submitSearchOnSearchForm($event: Event) {
    $event.preventDefault();

    if (this.searchBoxRef.nativeElement.value.trim()) {
      this.onClickSearchSubmit.emit(this.searchBoxRef.nativeElement.value);
      this.searchBoxRef.nativeElement.value = '';
    } else {
     this.searchBoxRef.nativeElement.placeholder = 'Поисковая строка пустая!';
     this.formSearchRef.nativeElement.style.border = '2px solid red';
     this.buttonSearchRef.nativeElement.style.backgroundColor = 'red';
     setTimeout(() => {
       this.searchBoxRef.nativeElement.placeholder = 'Искать на OZON';
       this.formSearchRef.nativeElement.style.border = '2px solid #005bff';
       this.buttonSearchRef.nativeElement.style.backgroundColor = '#005bff';
     },2000);
    }
  }
}
