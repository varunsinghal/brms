<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        
        <xsl:variable name="identifier" select="date-textbox/identifier" />
        <xsl:variable name="minDate" select="date-textbox/min-date" />
        <xsl:variable name="maxDate" select="date-textbox/max-date" />
        
        <div class="container mt-2">
            <div class="form-group">
                
                <label for="{$identifier}">
                    <xsl:value-of select="date-textbox/label"/> 
                </label>
                
                <input type="date" class="form-control form-control-sm" 
                       id="{$identifier}" min="{$minDate}" max="{$maxDate}"
                       name="{$identifier}" />
                
                <small class="form-text form-text-sm text-muted">
                    <xsl:value-of select="date-textbox/tooltip"/>
                </small>
                
            </div>
        </div>
        
    </xsl:template>
</xsl:stylesheet>
