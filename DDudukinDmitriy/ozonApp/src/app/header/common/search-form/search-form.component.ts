
import { Component, OnInit, ViewChild, ElementRef, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-search-form',
  templateUrl: './search-form.component.html',
  styleUrls: ['./search-form.component.css']
})

export class SearchFormComponent implements OnInit {
  @ViewChild('searchInput', { static: false }) clearRef: ElementRef
  @Output() search: EventEmitter<any> = new EventEmitter<any>();


  constructor() { }





  ngOnInit(): void {
  }

  public clearSearchInput(): void {
    this.clearRef.nativeElement.value = '';
  }

  public searchProduct(text) {
    this.search.emit(text);
  }
}
