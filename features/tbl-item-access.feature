Feature: Access table rows, columns, and cells
  In order to query and modify individual table items
  As an python-docx developer
  I need the ability to access table rows, columns, and cells

  Scenario: Access table row collection
     Given a table having two rows
      Then the length of its row collection is 2
       And each item in its row collection is a table row