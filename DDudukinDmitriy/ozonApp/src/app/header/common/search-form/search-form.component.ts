import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';

@Component({
  selector: 'app-search-form',
  templateUrl: './search-form.component.html',
  styleUrls: ['./search-form.component.css']
})
export class SearchFormComponent implements OnInit {
  constructor() { }
  @ViewChild('searchInput', { static: false }) clearRef: ElementRef
  ngOnInit(): void {
  }
  public clearSearchInput(): void {
    this.clearRef.nativeElement.value = '';
  }
}
